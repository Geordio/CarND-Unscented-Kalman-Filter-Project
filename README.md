# Unscented Kalman Filter Project Starter Code
Self-Driving Car Engineer Nanodegree Program

This document describes my solution for the Udacity Unscented Kalman Filter project in term 2 of the SDC nano degree


## Compiling

The project can be compiled by execting 'make' in the build directory.
The project has been developed on a linux environment

## Accuracy

When run against the simulator using Dataset 1, my implementation acheives a final RMSE of:
X: 0.0677
Y: 0.0844
VX: 0.3450
VY: 0.2356

A screenshot can be seen below:
![Simulator View](https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/writeup/simulator%20_screenshot.png  "Simulator View")

This satisifies the required target of .09, .10, .40, .30  respectively.

## Processing Flow

My implementation follows the general processing flow (as per the project skeleton code) of:
- Initialisation. Including initialisation of the state vectors from the first measurements
- Prediction
  - Generation of augmented sigma points
  - Prediction of sigma points
  - Predict mean and covariance
- Update
	- Predict the measurements
	- Update the states

In addition, I calculate the NIS values for LIDAR and RADAR, and store these in a file for visulisation.

## NIS Visulations

The NIS for the LIDAR and RADAR was visualised.
In order to perform this, the UKF.cpp stores the calculated NIS values in 2 log files. These log files are then parsed and visualised by the python file [nis_viz.py][e09286c2]

  [e09286c2]: https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/nis/nis_viz.py "nis_viz.py"

The visualisations of the NIS for LIDAR and RADAR are below.

![NIS LIDAR](https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/nis/NIS_plot_lidar.png)
![NIS RADAR](https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/nis/NIS_plot_radar.png)

In both instances the majority of the data  points are below the 95% confience line as per the project objectives.

## Code Efficency

I have not fully optimised the code yet I planned to implement a method to contain the common functionality of the LIDAR and RADAR update methods, but as yet I have not done this.
There is further optimisation that can be done, such as by removing the repeated calculations of the number of sigma points (an easy fix)
