# Assignment 2: CCD reductions and photometry

In this assignment you will work with a dataset of CCD images and perform basic data reduction (bias, dark, and flat-field corrections) and aperture photometry.

## Assignment link

To start working on the assignment, accept [this invitation](https://classroom.github.com/a/iTGW-QVL) which will create a private repository from the base template.

## Dataset

You can download the dataset from [this link](https://faculty.washington.edu/gallegoj/astr480/ccd_reductions_data.tar.bz2). You can then upload it to the JupyterHub environment, or you can download it directly there using the command:

```bash
wget https://faculty.washington.edu/gallegoj/astr480/ccd_reductions_data.tar.bz2
```

To uncompress the file run the command:

```bash
tar -xvzf ccd_reductions_data.tar.bz2
```

Inside the `ccd_reductions_data` folder you will find a [set of images taken with a CCD camera](https://zenodo.org/records/3245296). The images are in FITS format and include a set of bias, dark, and flat-field images, as well as a couple of science images. The file names indicate the type of image, and you can also check the header of each image to see the details of the observations.

Before you begin writing any code, spend some time looking at the images in the dataset in DS9 and familiarising yourself with the data and the header keywords.

## Goals and rubric

The ultimate goal of the assignment is to write a function that fully reduces a science frame, as well as to perform aperture photometry on locations on the image. The assignment is broken down into multiple files in the `src/ccd` directory, each one defining one or more functions that you need to implement. Each function has a docstring that describes what the function is expected to do and what it should output.

- **`bias.py`**: implement the function `create_median_bias()` which should take a set of bias frames and create a combined bias frame with sigma-clip rejection.
- **`dark.py`**: implement the function `create_median_dark()` which should take a set of dark frames and the median bias created in the previous step, and create a combined dark frame with the dark current levels per second.
- **`flat.py`**: implement the function `create_median_flat()` which should take a set of flat frames and the median bias and dark frames created in the previous steps, and create a combined flat frame with the flat-field correction. Implement the function `plot_flat()` to visualise the median flat-field frame.
- **`science.py`**: implement the function `reduce_science_frame()` which should take a science frame and the median bias, dark, and flat frames created in the previous steps, and create a reduced science frame. Optionally you can implement cosmic ray removal.
- **`photometry.py`**: implement the function `do_aperture_photometry()` which should take a reduced science frame and a list of aperture positions, a list of aperture radii, and the radius and width of the sky annulus, and perform aperture photometry on the image. Implement the function `plot_radial_profile()` to visualise the radial profile of the extracted aperture photometry.
- **`ptc.py`**: implement the functions `calculate_gain()` and `calculate_readout_noise()` to estimate the gain and readout noise of the CCD camera.
- **`reduction.py`**: implement the function `run_reduction()`. While the other functions ask you to take very specific inputs and produce a specific output, this function is free-form and you can think of it as a "script" that runs the entire reduction process. It must use the files in the dataset to fully reduce the two science frames included with the data and perform aperture photometry on at least one of them. The implementation will be evaluated based on how you use the function and any additional information that the function produces.

The grading rubric is as follows:

- `create_median_bias()`: up to 2 points if the implementation is correct.
- `create_median_dark()`: up to 2 points if the implementation is correct.
- `create_median_flat()`: up to 2 points if the implementation is correct.
- `plot_flat()`: up to 1 point if the implementation is correct.
- `reduce_science_frame()`: up to 3 points if the implementation is correct. 2 extra points if cosmic ray removal is implemented.
- `do_aperture_photometry()`: up to 4 points if the implementation is correct.
- `plot_radial_profile()`: up to 2 points if the implementation is correct.
- `calculate_gain()`: up to 2 points if the implementation is correct.
- `calculate_readout_noise()`: up to 2 points if the implementation is correct.
- `run_reduction()`: up to 5 points if the implementation is correct.

## Deadline

The assignment is due on Friday, May 16th at 11:59 PM. Late submissions by up to 24 hours will be penalized by 20% of the total points.

## Hints and resources

- It is likely that if you try to process the images in the JupyterHub environment you'll run out of memory. To prevent that, you can start by trimming your images and only keeping a small part of them (for example `[1536:2560, 1536:2560]` to get a 1024x1024 region centred on the image). Make sure that the resulting area is large enough to perform photometry of the stars that you're interested in, and that you include the overscan region if you are planning to use it.
- Remember to set up a virtual environment for your project using `uv sync` and activate it using `source .venv/bin/activate`.
- You should be able to complete the assignment using just `astropy`, `numpy`, `matplotlib`, and `photutils`. You are welcome to use any other libraries but you should not use `ccdproc` or other tools that directly perform the data reduction for you. Make sure that you use `uv add` to include any additional libraries that you need in your project.
- Make sure to check the expected inputs and outputs of each function in the docstring. Do not change the function names or the argument that they accept or the automated tests will not work.
- The automated tests (which you can run doing `pytest` from the root of your repository) will check that your functions are returning values with the expected format and type, but will not check that you are correctly implementing the methods. Be critical of the files that you are producing at each step. You can use DS9 to evaluate them visually.
- You can use [ASTROSCRAPPY](https://astroscrappy.readthedocs.io/en/latest/index.html) or [lacosmic](https://lacosmic.readthedocs.io/en/stable/) (or any other library you prefer) to implement cosmic ray removal. The best way to store the cosmic ray information is to add an extra extension to the output FITS file with the cosmic ray mask. Then you can take that mask into account when performing the aperture photometry.
- To determine the ideal sky aperture for aperture photometry you can use this approach: first examine the science frame in DS9 and identify a reasonable radius at which the star doesn't seem to be contributing a lot of signal; then run the `do_aperture_photometry()` function with a that radius and a reasonable width and plot the results with `plot_radial_profile()`. Does your selected radius look good? Is it too close to the star? Too far? Adjust the radius and width accordingly and repeat the process until you are happy with the results.
- Please, **write comments in your code**. Comments are critical to understanding any piece of code (good code should be at least 30% comments) and if your code doesn't fully work the comments can help us understand your thought process and what you wanted to achieve.
