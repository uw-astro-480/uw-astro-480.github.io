# Assignment 3: tabular data and data visualisation

In this assignment you will query Gaia DR3 data for an open cluster of your choice, plot an HR diagram (or CMD), and perform a simple isochrone fitting.

## Assignment link

To start working on the assignment, accept [this invitation](https://classroom.github.com/a/4xnOxtsC) which will create a private repository from the base template.

## Goals and rubric

The goal of this assignment is to use [astroquery](https://astroquery.readthedocs.io/en/latest/) to query Gaia DR3 data for an open cluster of your choice, analyse the data, plot an HR diagram (or CMD), and perform a simple isochrone fitting. First, you need to choose an open cluster to work with. You can choose any cluster you like but [here](https://en.wikipedia.org/wiki/List_of_open_clusters) is a list of some good candidates.

You'll need to implement five function in `src/tables/tables.py`. All the functions have docstrings that explain what you are expected to do in detail. Please read them carefully.

- **query_cluster_data()**: here you must retrieve the data for your cluster from Gaia DR3. We'll use [astroquery](https://astroquery.readthedocs.io/en/latest/) to do this. You can use the `gaia` module from `astroquery` to query the data. Essentially follow [these instructions](https://astroquery.readthedocs.io/en/latest/gaia/gaia.html#cone-search) to perform a cone search around the cluster coordinates. You must also remove rows without known distance.
- **plot_histogram()**: read the data for the cluster and plot a histogram of the distance distribution.
- **plot_hr_diagram()**: read the data for the cluster and plot a Hertzsprung-Russell diagram (or CMD) of the cluster using a 2D histogram or KDE. Make sure that you use only stars that are expected to belong to the cluster.
- **plot_isochrone()**: read the data for the cluster and from a library of isochrones (refer to the docstring for details on what isochrones are and the format of the files), plot again the HR diagram, and plot the isochrone that best fits the data.
- **plot_anything()**: this is a free-form function where you can read the data from the cluster and plot anything that you like (one or multiple plots).

The grading rubric is as follows:

- `query_cluster_data()`: up to 2 points.
- `plot_histogram()`: up to 2 points.
- `plot_hr_diagram()`: up to 3 points.
- `plot_isochrone()`: up to 5 points.
- `plot_anything()`: up to 3 points. Grading is awarded based on the originality and quality of the plot.

## Deadline

The assignment is due on Wednesday, June 4th at 11:59 PM. Late submissions by up to 24 hours will be penalized by 20% of the total points.

## Hints and resources

- Remember to set up a virtual environment for your project using `uv sync` and activate it using `source .venv/bin/activate`.
- You can use any libraries that you want in this project. `astroquery` will return an Astropy table. You can continue using that or use Polars or Pandas. Similarly you can use any plotting library you want. I recommend using [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/) but you are free to use any library you like.
- Make sure to check the expected inputs and outputs of each function in the docstring. Do not change the function names or the argument that they accept or the automated tests will not work.
- The automated tests (which you can run doing `pytest` from the root of your repository) will check that your functions are returning values with the expected format and type, but will not check that you are correctly implementing the methods. Be critical of the files that you are producing at each step. You can use DS9 to evaluate them visually.
- Please, **write comments in your code**. Comments are critical to understanding any piece of code (good code should be at least 30% comments) and if your code doesn't fully work the comments can help us understand your thought process and what you wanted to achieve.
- You can commit Jupyter Notebooks that you used to develop your code as long as you do so in the `notebooks/` folder. You won't be able to commit them anywhere else. If you code implementation fails we will check that folder to see if you have any Jupyter Notebooks that can help us understand your thought process and what you wanted to achieve.
