---
file_format: mystnb
kernelspec:
  name: python3
mystnb:
  merge_streams: true
  execution_timeout: 300
---

```{code-cell} ipython3
%matplotlib inline

import os
import seaborn
from astropy.io import fits
from astropy.visualization import ZScaleInterval, ImageNormalize, LinearStretch
from matplotlib import pyplot as plt

seaborn.set_palette('deep', color_codes=True)
plt.ion()

# Change these paths to point to the location of your data
LFC_DIR = '../../data/example-cryo-LFC/'
ANDOR_DIR = '../../data/ccd_reductions_data/'

# This moves the current working directory to the location of the LFC data
os.chdir(LFC_DIR)
```

# Photometry and CCD calibrations

Once your data has been taken and [reduced](#basic-ccd-reductions) it is the time to perform analysis on it. The scope of that analysis will depend on the type of data and the science goals of your project. Here we will focus on two main topics: aperture photometry and astrometric registration.

## Aperture photometry

At its core aperture photometry is just summing up the pixels values around a give position or source. The term "aperture" refers to the geometric shape (usually circular but potentially a ellipse or a polygon) used to define the area of the image that will be summed. It is possible to do aperture photometry by hand, but there are subtleties such as the handling of background noise and subpixel regions that are not totally trivial. Because of that we will use a package, [photutils](https://photutils.readthedocs.io/en/stable/), that implements many of the algorithms and methods used in aperture photometry. Note that `photutils` is not, by far, the only package available that can do this, and that its scope is larger than just aperture photometry.

For the purposes of this tutorial we will use the image `ccd.037.0_proc.fits` that we created in the [basic CCD reductions](#basic-ccd-reductions-science) section.

```{code-cell} ipython3
ccd37_proc = fits.open('ccd.037.0_proc.fits')
ccd37_proc_data = ccd37_proc[0].data.astype('f4')

# Plot the flat image
norm = ImageNormalize(ccd37_proc_data, interval=ZScaleInterval(), stretch=LinearStretch())
_ = plt.imshow(ccd37_proc_data, origin='lower', norm=norm, cmap='YlOrBr_r')
```

### Source detection

Often we know what sources we want to measure on an image, but its also common to want to measure all the available sources, or those that match some criteria. While detecting sources is something the human eye and brain are quite good at, it's not trivial to implement a computer algorithm that can do this in a robust and efficient way. [photutils.detection](https://photutils.readthedocs.io/en/latest/user_guide/detection.html) provides to well tested algorithms for quickly (but somewhat loosely!) identifying sources in an image: `DAOStarFinder` and `IRAFStarFinder`. Both of these algorithms are based on the idea of convolving the image with a kernel that is sensitive to point sources. We will use `DAOStarFinder` here with a very basic configuration, but note that it's important to understand the parameters of the algorithm and how they affect the results.

`DAOStarFinder` requires defining two parameters: the `fwhm` of the sources, and the noise `threshold` above which we consider a pixel to be a part of a region. The `fwhm` parameter is the full width at half maximum of the Gaussian kernel used to convolve the image and its somewhat less critical as long as it's not larger than the real FWHM of the image. This value must be given in pixels. Since the pixel scale of the LFC camera is ~ 0.18 arcsec/pixel, if we assume an average seeing of 1 arcsec, the FWHM of the sources in the image is about 5 pixels.

To determine the threshold we can use `sigma_clipped_stats` from `astropy` to get mean, median, and standard deviation of a blank region on the image. Here we are interested in the standard deviation, which is a measure of the background noise after the reduction process.

```{code-cell} ipython3
from astropy.stats import sigma_clipped_stats

# Select a blank region of the image
data_blank = ccd37_proc_data[1000:1100, 800:1000]

# Calculate the mean, median and standard deviation of the blank region
mean, median, std = sigma_clipped_stats(data_blank, sigma=3.0)
print(f'Mean: {mean:.2f}, Median: {median:.2f}, Std: {std:.2f}')
```

Now let's use these values to run `DAOStarFinder`. We will set the threshold to 5 times the standard deviation, which is a good starting point to detect sources that are likely to be real. Note that we will subtract the median background from the image before running the source detection algorithm. This is important in cases where the background is significant.

```{code-cell} ipython3
from photutils.detection import DAOStarFinder

# Run DAOStarFinder
daofind = DAOStarFinder(fwhm=5.0, threshold=5*std)
sources = daofind(ccd37_proc_data - median)

print(sources)
```

The result is an astropy [table](https://docs.astropy.org/en/stable/table/index.html) in which each row corresponds to a detected source. The columns of the table contain the x and y coordinates of the sources, as well as their fluxes and other properties. Note that the magnitudes and fluxes here are instrumental (based on ADU values) and not calibrated. The `xcentroid` and `ycentroid` columns are the positions of the sources in pixels.

```{important}
The centroids returned by `DAOStarFinder` are determined using a algorithm that is efficient but not very precise. It is recommended that you recalculate these centroids using a more precise algorithm, as we will see in the next section.
```

Let's plot the detected sources on top of the image.

```{code-cell} ipython3
_ = plt.imshow(ccd37_proc_data, origin='lower', norm=norm, cmap='YlOrBr_r')

# Plot the detected sources
_ = plt.scatter(sources['xcentroid'], sources['ycentroid'], s=10, c='red', marker='x')

# Zoom on a region of the image for better visibility

_= plt.xlim(500, 1500)
_ = plt.ylim(1000, 2000)

```

Note that while most of the source that we have detected look like real stars (or sometimes galaxies), there are also many sources that we have not identified. These regions are either too faint (they can be recovered by reducing the threshold) or are not well fit by a Gaussian profile (like extended galaxies). You may also find that some of the sources have multiple detections. This usually happens when the FWHM is not properly defined but can also happen in very bright, saturated sources.

### Centroiding

Next, let's look at better ways to determine the centroid of our sources. The easiest, naive approach to this problem would be to just select the pixel with the maximum value in the region we are interested in. This has two problems: first, we may have spurious signal in some pixels (for example cosmic rays) that are not part of the source and that affect our centroiding; and second, this only allows us to determine the centroid to the integer pixel value level, which is not very precise. A better approach is to assume that the source of interest follows a given profile (usually a Gaussian or a Lorentzian for point source ---stars, but the profile may be different for other types of object and depending on our optical system) and fit the profile function to the data. This is technically the most precise way to determine the centroid, but it is also the most computationally expensive.

In the middle sit a number of algorithm that try to find a balance between speed and precision. The package [photutils.centroids](https://photutils.readthedocs.io/en/latest/user_guide/centroids.html) implements a number of these algorithms. Their use is similar so here we will use the `centroid_1dg` algorithm, which fits 1D Gaussians to the x and y marginal distributions of the source (you can think of this as "collapsing" the source along the x and y axes and then fitting a Gaussian to the resulting 1D distributions). This is a good compromise between speed and precision, and it is also very robust to noise.

For this we will use one of the source we detected in the previous step at $x\sim999$ and $y\sim1932$.

```{code-cell} ipython3
from photutils.centroids import centroid_1dg

# Centroids of the source from DAOStarFinder
xd = 999.2980968694505
yd = 1932.5177532355156

# Get a small region around the source

x0 = int(xd)
y0 = int(yd)
data = ccd37_proc_data[y0-10:y0+10, x0-10:x0+10]

# Calculate the centroid using the 1D Gaussian algorithm.
# It's important to remove the median background!
xc, yc = centroid_1dg(data - median)

# This centroid is with respect to the region we selected, so we need to add the offset
xc += (x0 - 10)
yc += (y0 - 10)

print(f'Centroid: {xc:.2f}, {yc:.2f}')

# Let's plot the two centroids estimates.
norm = ImageNormalize(data, interval=ZScaleInterval(), stretch=LinearStretch())
_ = plt.imshow(data, origin='lower', norm=norm, cmap='YlOrBr_r')
_ = plt.scatter(xd - x0 + 10, yd - y0 + 10, s=100, c='red', marker='x', label='DAOStarFinder')
_ = plt.scatter(xc - x0 + 10, yc - y0 + 10, s=100, c='blue', marker='x', label='Centroid 1D Gaussian')
_ = plt.legend()
```

As you can see the difference is often at the subpixel level, but that can be important depending on the analysis that you are trying to perform.

### Simple aperture photometry

Now that we have the exact centroid of our source we can actually perform aperture photometry. We'll start by defining a circular aperture with a radius of 10 pixels. [photurils.aperture](https://photutils.readthedocs.io/en/latest/user_guide/aperture.html) provides a number of aperture shapes, including circular, elliptical, and annular. We will use the `CircularAperture` class to define our aperture.

```{code-cell} ipython3
from photutils.aperture import CircularAperture

# Define the aperture
aperture = CircularAperture((xc, yc), r=10)

# Plot the aperture on top of the image
_ = plt.imshow(ccd37_proc_data, origin='lower', norm=norm, cmap='YlOrBr_r')
_ = aperture.plot(color='red', lw=2, label='Aperture')
_ = plt.xlim(900, 1100)
_ = plt.ylim(1800, 2100)
```

So far we have not extracted any data from the image, we have just defined an abstraction of a circular aperture. To actually extract the data we need to use the `aperture_photometry` function.

```{code-cell} ipython3
from photutils.aperture import aperture_photometry

# Perform aperture photometry
phot_table = aperture_photometry(ccd37_proc_data - median, aperture)
print(phot_table)
```

The resulting table contains the x and y centroids that we provided (we defined an aperture for a single region but it would have been possible to define the same aperture for multiple regions) and the total sum of the pixels in the aperture. Note that we again subtracted the median background since that is signal that is not part of our source.

Let's consider the case in which we want to measure the flux on the same region using apertures with multiple radii. For that we need to define multiple apertures and pass them to `aperture_photometry`.

```{code-cell} ipython3
# Define the apertures between r=1 and r=50
radii = range(1, 51, 1)
apertures = [CircularAperture((xc, yc), r=r) for r in radii]

# Perform aperture photometry
phot_table = aperture_photometry(ccd37_proc_data - median, apertures)

print(phot_table)
print(phot_table.colnames)
```

There `phot_table` table now contains a column for each one of the apertures we defined. We can plot the growth curve with a bit of table manipulation.

```{code-cell} ipython3
# Get the region we are interested in from the table
region = phot_table[0]

# Convert the values to a list
region_data = list(region.values())

# Exclude the first three values, which are the id, x, and y coordinates
fluxes = region_data[3:]

# Plot the growth curve
_ = plt.plot(radii, fluxes, marker='o')
_ = plt.xlabel('Aperture radius (pixels)')
_ = plt.ylabel('Flux (ADU)')
```

:::{note}
Although we won't discuss the details here, `photutils.aperture` also provides aperture classes that can be defined using sky coordinates (RA, Dec) instead of pixels, assuming that the image has the proper WCS information. Other than how the aperture is defined, the rest of the process is the same.
:::

### Local background subtraction

In the previous growth curve we saw that the flux grows with the aperture but never really plateaus. This is because, although we are subtracting the median image background, the background around the source is likely different and we are not properly estimating it. A better approach is to measure the background around our source using an annular aperture with a radius that is large enough to make sure that it does not include any of the source signal but is not so large as to not being representative of the local background. The best radius can be determined by eye or, better, using a radial profile as we will see in the next section. For now we will use an annulus with an inner radius of 30 pixels and a width of 5 pixels, which according to the previous plots should work well enough.

```{code-cell} ipython3
from photutils.aperture import CircularAnnulus

# Define the annulus
annulus = CircularAnnulus((xc, yc), r_in=30, r_out=35)

# Plot the annulus
_ = plt.imshow(ccd37_proc_data, origin='lower', norm=norm, cmap='YlOrBr_r')
_ = annulus.plot(color='blue', lw=2, label='Annulus')
_ = plt.xlim(900, 1100)
_ = plt.ylim(1800, 2100)
```

Now let's perform aperture photometry on the annulus and estimate the background. We could do this manually but instead we will use the `ApertureStats` class.

```{code-cell} ipython3
from photutils.aperture import ApertureStats

annulus_stats = ApertureStats(ccd37_proc_data, annulus)
back = annulus_stats.median
print(f'Background per pixel: {back:.3f}')
```

Now we can use define a region around our source and subtract this background. The best way to do this is to calculate the raw flux and then subtract the background multiplied by the area of the aperture.

```{code-cell} ipython3
aperture = CircularAperture((xc, yc), r=30)

phot_table = aperture_photometry(ccd37_proc_data, aperture)
flux = phot_table['aperture_sum'][0]
aperture_area = aperture.area_overlap(ccd37_proc_data)
flux_no_back = flux - back * aperture_area

print(f'Flux (raw): {flux:.3f}')
print(f'Background: {back:.3f}')
print(f'Area: {aperture_area:.3f}')
print(f'Flux (without background): {flux_no_back:.3f}')
```

The resulting flux, after subtracting the background, is much lower than the raw flux. The background in this image is very significant (this is not the bias or dark levels, we removed those, but the sky background) and it's critical to subtract it properly.

Let's repeat our growth curve analysis but using the local background subtraction.

```{code-cell} ipython3
radii = range(1, 31, 1)
apertures = [CircularAperture((xc, yc), r=r) for r in radii]

# Calculate the raw flux for each aperture
phot_table = aperture_photometry(ccd37_proc_data, apertures)
region = phot_table[0]
region_data = list(region.values())
fluxes = region_data[3:]

# For each aperture estimate the area and subtract the background
fluxes_no_back = []
for i, r in enumerate(radii):
    aperture = apertures[i]
    aperture_area = aperture.area_overlap(ccd37_proc_data)
    flux_no_back = fluxes[i] - back * aperture_area
    fluxes_no_back.append(flux_no_back)

# Plot the growth curve
_ = plt.plot(radii, fluxes_no_back, marker='o')
_ = plt.xlabel('Aperture radius (pixels)')
_ = plt.ylabel('Flux (ADU)')
```

That's significantly better! This also tells us that probably all the flux in our source is contained in a radius of about 15 pixels (of course we can define this more precisely by, for example, estimating when the cumulated flux increases by less than 1%).

### Radial profile

Coming soon.

## Astrometric registration

Coming soon.
