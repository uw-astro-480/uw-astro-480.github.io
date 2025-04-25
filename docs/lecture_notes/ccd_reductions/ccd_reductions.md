---
file_format: mystnb
kernelspec:
  name: python3
mystnb:
  execution_mode: 'inline'
---

# Basic CCD reductions

:::{important}
This sections is a work in progress. New content will be added shortly.
:::

"Reduction" is the term used to describe the general process of taking raw data from a CCD camera and performing a series of operations to produce a final image in which we have removed as many of the systematic trends and defects that affect the original image. Very generally, the steps in the reduction process are:

- Bias subtraction
- Dark correction
- Flat field correction
- Cosmic ray removal
- Bad pixel masking

Often there are other steps such as astrometric and photometric calibration that are part of the reduction process, but we will discuss those at a later time.

## Datasets

For this lecture we will use a [set of images](https://doi.org/10.5281/zenodo.3254683) taken using the Palomar Large Format Camera (LFC) on the Hale 200-inch telescope. Technical details about the camera can be found [here](https://sites.astro.caltech.edu/palomar/observer/200inchResources/lfcspecs.html). The dataset include several bias, flat, dark, and science images from one of the 6 detectors in the LFC mosaic, and can be downloaded from [here](https://zenodo.org/record/3254683/files/example-cryo-LFC.tar.bz2?download=1).

We will also use another [set of images](https://zenodo.org/records/3245296) from an Andor Aspen CG16M camera. You can download them [here](https://zenodo.org/record/3245296/files/example-thermo-electric.tar.bz2?download=1). After you download the datasets and copy them to the location where you want to use them, you can decompress them by doing

```bash
tar cjvf example-cryo-LFC.tar.bz2
```

Many of the steps in this lecture follow the structure of the [CCD Data Reduction Guide](https://www.astropy.org/ccd-reduction-and-photometry-guide/v/dev/notebooks/00-00-Preface.html) which uses the same datasets.

:::note
You can download this lecture as {nb-download}`ccd_reductions.ipynb` or {download}`ccd_reductions.md` and follow along. For that make sure that you change the values of the `LFC_DIR` and `ANDOR_DIR` variables to point to the directory where you have your data.
:::

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline

from astropy.io import fits
from matplotlib import pyplot as plt

plt.ion()

LFC_DIR = '../../data/example-cryo-LFC/'
ANDOR_DIR = '../../data/ccd_reductions_data/'
```

## Bias and overscan

Analog-to-digital converters (ADC) require the signal that they work with to have a positive charge. To avoid cases in which this could be a problem, a small _bias_ voltage is added to the output signal before it reaches the ADC. Ideally this bias level would be constant, but in practice the level varies by small amounts from pixel to pixel and during the night as the outside temperature changes.

Our first step in the reduction process is to remove the contribution from the bias level by measuring its median level and subtracting it from any other image we have taken that night (_all_ images are affected by the bias level, not only science frames). To achieve this there are typically two alternatives: the use of a series of zero-exposure images (bias frames) or using a special part of the image called the _overscan_ region.

### Bias frames

Bias frames are images that are taken with zero exposure time and the shutter closed. Most cameras have a special mode to take these image. With no exposure time there is no signal (photons) reaching the surface of the CCD, so the only things that we are reading as we generate the digital image is the bias level and the readout noise (and a small amount of dark current that, if the camera is properly cooled, is usually negligible). From a bias frame the average value across the image (mean, median, mode) is an estimate of the bias level while the standard deviation gives us the readout noise.

In the LFC dataset the bias frames are images 1 to 6. Let's open one of them:

```{code-cell} ipython3
bias = fits.open(LFC_DIR + 'ccd.001.0.fits')
bias.info()
```

The image contains a single extension or HDU, with an image frame that is 2080, 4128 pixels and a header with 43 keywords. Let's quickly look at the header:

```{code-cell} ipython3
bias[0].header
```

The header tells us useful stuff about the instrument, when this image was taken, etc. The last few keywords are useful for data reduction. `CCDSEC` and `DATASEC` tells use the region of the image that contains valid data, while `BIASSEC` tells us where the overscan region is located. These keywords are a legacy from a reduction software called [IRAF](https://iraf-community.github.io/), which is still used by many astronomers.

:::warning
The pixel values in `DATASEC` and others are 1-indexed, while in Python we use 0-indexed arrays.
:::

Let's now look at one of the images. We will use some tools in [astropy.visualization](https://docs.astropy.org/en/stable/visualization/normalization.html) to normalise the image for display:

```{code-cell} ipython3
from astropy.visualization import ImageNormalize, LinearStretch, ZScaleInterval

data = bias[0].data.astype('f4')
norm = ImageNormalize(data, interval=ZScaleInterval(), stretch=LinearStretch())

image = plt.imshow(data, origin='lower', norm=norm, cmap='gray')
```

Note that before I started doing anything to the image I converted the data to a `float32` array by doing `.astype('f4')` (I could have also done `.astype(numpy.float32)`). Normally raw CCD frames are encoded as unsigned-integer 16-bit, which is enough to containe the values 0-65,535 that 16-bit ADC generate, but that data format can cause problems ---mainly due to overflow--- once we start doing operations on them.

We can see several things in the image. First, it is quite flat, as we would expect, but there is a significant gradient on the left side. This is probably due to electronic noise if the readout hardware is on that part of the chip. Let's have a look at how significant this gradient is. Let's collapse the image along the y-axis (the first axis in the `numpy` array, remember that `numpy` arrays are 0-indexed and arranged such that the first axis is rows and the second axis is columns) and plot the result:

```{code-cell} ipython3
import numpy

# Collapse the image along the y-axis
bias_profile = numpy.median(data, axis=0)

# Plot the result and focus on the left side of the images. The _ = are a trick to
# avoid printing the result of the plot command.
_ = plt.plot(bias_profile)
_ = plt.xlim(-20, 1000)
```

Most of the image has a fairly constant bias level of about 1140 but the left side gradient reaches over 1350 counts. We'll want to avoid this region by trimming or ignoring the first 300-400 pixels of the image (unless we can proof that this gradient is very constant over time and we can correct for it).

Let's now quickly look at the average levels (bias) and the standard deviation (readout noise) of the image. We will use the median which is more robust against outliers than the mean. For these images in which all values are integers the mode is also a good choice.

```{code-cell} ipython3
bias = numpy.median(data)
readout_noise = numpy.std(data)

print(f'Bias: {bias} counts')
print(f'Readout noise: {readout_noise:.2f} counts')
```

This approximately matches what we saw in the profile plot. However we are averaging over the entire image, which includes the overscan region and also the gradient. In general it is always a good idea to use smaller regions that we have confirmed are not affected by any systematic effects. Let's repeat the calculation but by taking a smaller region around $(2000, 1000)$.

```{code-cell} ipython3
# Define the region of interest. Note that the first axis is y and the second axis is x.
region = data[1000:1500, 2000:2500]

bias = numpy.median(region)
readout_noise = numpy.std(region)

print(f'Bias: {bias} counts')
print(f'Readout noise: {readout_noise:.2f} counts')
```

The bias level has not changed much but the readout noise has decreased dramatically! This is not unexpected since we are not averaging over a very flat region that should only be affected by the readout noise. Note that both the bias level and readout noise here are measured in counts or ADU. We will see later how to convert these values to electrons.

### CCD corrections are noisy

An important concept to remember is that **it is not possible to remove noise from an image**. Here "noise" refers to the random fluctuations in the pixel values due to statistical noise (for example the Poisson or "shot" noise inherent to the arrival of photons). Sometimes noise is also used to refer to systematic effects that are we see in the image, such as the bias level or the flat field. The latter are the trends that we can measure and correct for, but the noise that they introduce (e.g., the readout noise) cannot be removed. In fact, applying a correction to an image will always add noise to the image unless the correction is perfect, which is hardly ever the case.

The best way to avoid compounding our noise problem is by using corrections that introduce as little noise as possible. One way to achieve this is to take multiple images for each type of correction and combine them. Error propagation theory tells us that when we average multiple images with the same noise level the resulting image has a noise level that is reduced by a factor of $\sqrt{N}$, where $N$ is the number of images. Let's prove that.

We start by creating an image with a known mean level and noise. We'll draw the values from a Gaussian distribution with mean 500 and standard deviation 10. This can be done easily using `scipy` and `numpy` but we'll use the function [make_noise_image](https://photutils.readthedocs.io/en/stable/api/photutils.datasets.make_noise_image.html) from `photutils`.

```{code-cell} ipython3
from photutils.datasets import make_noise_image

# Create a noise image with a mean of 500 and standard deviation of 10
noise_image = make_noise_image((1000, 1000), mean=500, stddev=10, distribution='gaussian')

print(noise_image.shape)
print(f'Mean: {numpy.mean(noise_image):.5f}')
print(f'Standard deviation: {numpy.std(noise_image):.5f}')
```

Now we'll create multiple of these image and average them. To do that we create a list which we then convert into a 3D array. We can then use `numpy.mean` to calculate the mean along the first axis. This will result in a 2D image with the same shape as the original images in which each pixels is the average of the values in that pixel across all images.

```{code-cell} ipython3
# Create a list of noise images
noise_images = [make_noise_image((1000, 1000), mean=500, stddev=10, distribution='gaussian') for _ in range(5)]
print(f'Number of images: {len(noise_images)}')

# Convert the list into a 3D array
noise_images_3d = numpy.array(noise_images)
print(f'Shape of the 3D array: {noise_images_3d.shape}')

# Calculate the mean along the first axis
mean_image = numpy.mean(noise_images_3d, axis=0)
print(f'Shape of the mean image: {mean_image.shape}')

# Calculate the mean and standard deviation of the resulting image
mean = numpy.mean(mean_image)
stddev = numpy.std(mean_image)

print(f'mean: {mean:.5f}')
print(f'Standard deviation: {stddev:.5f}')
```

As expected the mean has not changed but the standard deviation has decreased. From an original standard deviation of 10 for each image we would expect the resulting image to have a standard deviation of $10/\sqrt{5} = 4.472$ which is very close to what we see.

:::warning
This example does not work as well if you use the median instead of the mean. The $\sqrt{N}$ factor only applies to the mean, which the standard deviation of the mean decreasing as $N$ increases but more slowly then with the mean.
:::

### Combining multiple images

Let's now combine several real bias frames and look at the resulting image. The process is similar to what we saw above but now we'll open all images 1-6 from our dataset:

```{code-cell} ipython3
bias_images = []

for i in range(1, 7):
    bias_data = fits.getdata(LFC_DIR + f'ccd.00{i}.0.fits')
    bias_images.append(bias_data.astype('f4'))

# Convert the list into a 3D array
bias_images_3d = numpy.array(bias_images)
bias_mean_2d = numpy.mean(bias_images_3d, axis=0)

# Calculate the median and standard deviation on a small region
region = bias_mean_2d[1000:1500, 2000:2500]
bias_median = numpy.median(region)
bias_std = numpy.std(region)

print(f'Median: {bias_median:.2f}')
print(f'Standard deviation: {bias_std:.2f}')
```

The bias level has decreased a bit, which we can explain as some outliers (mostly cosmic rays as we'll see later) getting averaged out. The standard deviation has also decreased, as we expected from the previous section. Instead od the expected $3.82/\sqrt{6}\sim 1.56$ we see a higher value of $\sim 2$. This tells us that the distribution of the bias noise is not perfectly Gaussian, which is not unexpected. This example shows that there is a limit to how much we can reduce the noise by averaging real images. During observations we'll want to take as many bias (and other calibration frames) as possible but taking into account that there is a trade-off between the time we spend taking these images and the time we spend taking science images.

There is however another trick that we can employ when combining images. So far we have treated all images equally, and there is not reason not to do so. But at the pixel level we will often found that the value for that pixel in one image is significantly different from the others. This can be caused by cosmic rays or electronic misbehaviours. We would like to be able to identify those outliers and ignore them when calculating the combined image. The solution is what we call _sigma-clipping_.

With sigma-clipping the idea is that for each pixel we take all the values that contribute to the combined pixel and calculate the median (or mean or mode) and the standard deviation. Then we determine how many times the standard deviation each value is with respect to the median. If a values is away from the median by more than a certain number of standard deviations we consider it an outlier and reject it. We then repeat the process iteratively until there are no more outliers (or we reach a minimum number of points that we want to keep). The resulting image will be the median of the original images but with a strong robustness against outliers.

It's easy to implement a sigma-clipping algorithm in Python (and you should try it!) but for convenience we can use `astropy`'s implementation in [astropy.stats.sigma_clip](https://docs.astropy.org/en/stable/api/astropy.stats.sigma_clip.html)

```{code-cell} ipython3
from astropy.stats import sigma_clip

# Call sigma_clip with a threshold of 2.5 sigmas and using the median as the central function.
# The result is a list of masked arrays in which pixels that are outliers are masked.
# Note that we need to use the axis=0 argument to tell sigma_clip that we want
# to apply it along the first axis.
bias_images_masked = sigma_clip(bias_images, cenfunc='median', sigma=2.5, axis=0)

print(f"Number of elements: {len(bias_images_masked)}")
print(f"Type of the first element: {type(bias_images_masked[0])}")
print(f"Number of pixels masked in the first image: {bias_images_masked[0].mask.sum()}")
```

You can try the previous code with different values of `sigma` and see how the number of masked pixels changes. Now let's create the combined image using the masked arrays.

```{code-cell} ipython3
# Calculate the mean along the first axis. We use the ma module
# to handle masked arrays correctly.
bias_sc_mean_2d = numpy.ma.mean(bias_images_masked, axis=0)
print(f"Shape of the combined image: {bias_sc_mean_2d.shape}")
print(f"Type of the combined image: {type(bias_sc_mean_2d)}")

# Calculate the mean and standard deviation on a small region.
region = bias_sc_mean_2d[1000:1500, 2000:2500]
bias_mean = numpy.ma.mean(region)
bias_std = numpy.ma.std(region)

print(f'Mean: {bias_mean:.2f}')
print(f'Standard deviation: {bias_std:.2f}')
```

We see a slight increase in our estimation of the readout noise. This is not unexpected since now many mean pixel values are being calculated from fewer images. This process may need to be repeated with several values of the sigma-clip threshold until a good compromise is found between robustness against outliers and not discarding too many images.

:::note
Although we have used it with a set of 2D images here, the `sigma_clip` function can be used with any n-dimensional array.
:::

### Overscan region

The overscan region is an area of the CCD image in many professional cameras. It is generated by reading "fake" pixels that are not part of the real image (i.e., they do not correspond to any physical pixels on the CCD). This is done by telling the readout electronics to continue reading a number of pixels after each row in the serial register. Since these pixels are not really part of the image, what we read is just the contribution of the bias level and the readout noise generated by the readout electronics.

Overscan regions are useful because of two reasons:

- They are a very good estimate of the bias level at each row that is unaffected by differences between pixels.
- It is taken with each image (regardless of the type of exposure and exposure time) so it can be used to track the changes in the bias level during the night.

There are also a few caveats to the use of the overscan region:

- The overscan region is only a few pixels wide per row, so our statistics of the bias level will be poorer. In general it is not a good idea to use the overscan region to estimate the readout noise.
- If the bias level changes across the row the overscan region may not be able to track it.

With these pros and cons in mind, let's look at the overscan region of one of our images. The `BIASSEC` keyword in the header tells us that the overscan region in the LFC images is located at the end of each row (the last $\sim 30$ columns of each row). However if we zoom on that region on a bias frame we won't see anything special. That's expected since the bias and overscan should have the same levels. Instead, let's use a flat image which we'll describe later. For now we just need to know that this is an image created with a uniform illumination of the CCD and relatively high signal levels. Images 14-19 in the LFC dataset are flat images.

```{code-cell} ipython3
from astropy.visualization import ZScaleInterval

flat = fits.open(LFC_DIR + 'ccd.014.0.fits')
flat_data = flat[0].data.astype('f4')

# Plot around the overscan region.
overscan_zoom = flat_data[:, 2000:]

norm = ImageNormalize(overscan_zoom, interval=ZScaleInterval(), stretch=LinearStretch())
_ = plt.imshow(overscan_zoom, origin='lower', norm=norm, cmap='YlOrBr')
_ = plt.ylim(0, 4128)
```

:::note
In reality it seems that this camera has two overscan regions, one at the end of each row and one at the end of each column. Since the header recommends using the overscan region at the end of each row, we will use that one.
:::

Let's take vertical and horizontal profiles of the overscan region to see how flat it is.

```{code-cell} ipython3
# Select the overscan region. Remove some pixels from the edges to avoid weird effects.
overscan = flat_data[20:-20, 2048:]

# Collapse the image along the x-axis and plot the result
overscan_profile_x = numpy.mean(overscan, axis=1)
_ = plt.plot(overscan_profile_x)
```

We see that the overscan is reasonably flat but there are some fluctuations as we move along the y-axis. They are, however, smooth variations which may lead us to believe that they are real. Let's check the other direction.

```{code-cell} ipython3
overscan_profile_y = numpy.mean(overscan, axis=0)

_ = plt.plot(overscan_profile_y)
```

It seems the overscan does not really start at index 2048 as we expected, and that for the first few pixels in each row it decreases until it reaches a more constant value. This is a normal behaviour, caused by residual charge from previous pixels in the row. Let's ignore the first 5 pixels in each overscan row.

```{code-cell} ipython3
overscan = flat_data[20:-20, 2053:]
overscan_profile_y = numpy.mean(overscan, axis=0)

_ = plt.plot(overscan_profile_y)
```

This looks better but note the sawtooth pattern, which is caused by the small number of pixels that contribute to the value in each column. Overall, if we wanted to use the overscan region from this image we probably would want to use the regions between 2058 and 2068 pixels approximately.
