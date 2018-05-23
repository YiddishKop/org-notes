# SciPy2017 tutorial: Introduction to Numerical Computing with NumPy
#### Presented by: [Dillon Niederhut](https://dillon.niederhut.us), [Enthought Inc.](https://www.enthought.com)

This repository contains all the material needed by students registered for the
Numpy tutorial of SciPy 2017 on Tuesday, July 11th 2017.

For a smooth experience, you will need to make sure that you install or update
your Python distribution and download the tutorial material _before_ the day
of the tutorial as the Wi-Fi at the AT&T center can be flaky.


## Install Python

If you don't already have a working python distribution, you may download
Enthought Canopy ([https://store.enthought.com/](https://store.enthought.com/),
Anaconda Python ([http://continuum.io/downloads](http://continuum.io/downloads)),
or Python.org  ([https://www.python.org/downloads/](https://www.python.org/downloads/)).


## Install Packages

To be able to run the examples, demoes and exercises, you must have the
following packages installed:

- numpy 1.11+
- matplotlib 2.0+
- ipython 5.0+ (for running, experimenting and doing exercises)

With Canopy, the required packages are already installed. If you are using Python from python.org or your system, you can install the necessary packages with:

```sh
pip install -U numpy matplotlib ipython
```

If you are using Anaconda, you can install the necessary packages with:

```sh
conda install numpy matplotlib ipython
```

To test your installation, please execute the `check_env.py` script.

```sh
$ python check_env.py
```

You should see a window pop up with a plot that looks vaguely like a smiley face.

## Download Tutorial Materials

This GitHub repository is all that is needed in terms of tutorial content. The simplest solution is to download the material using this link:

https://github.com/enthought/Numpy-Tutorial-SciPyConf-2017/archive/master.zip

If you're familiar with Git, you can also clone this repository with:

```sh
$ git clone https://github.com/enthought/Numpy-Tutorial-SciPyConf-2017.git
```

It will create a new folder named SciPy2017_numpy_tutorial/ with all the
content you will need: the slides I will go through (`slides.pdf`), and a folder
of exercises.


## Questions? Problems?

You may post messages to the slack channel for this tutorial at: [https://scipy2017.slack.com](https://scipy2017.slack.com)
