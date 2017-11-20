# Unscented Kalman Filter Project Starter Code
Self-Driving Car Engineer Nanodegree Program

This document describes my solution for the Udacity Unscented Kalman Filter project in term 2 of the SDC nano degree


## Compiling

The project can be compiled by execting 'make' in the build directory.
The project has been developed on a linux environment

## implementation

The following C++ files were modified to implement my solution:

File  |  Description
--|--
ukf.cpp & ukf.h  |  implement the UKF pipeline, including Initialisation, Prediction and Update steps
tools.cpp  |  Implement the RMSE method

In addition, a python file, nis_viz.py, to visualise the NIS was created.

## Accuracy

When run against the simulator using Dataset 1, the results below are acheived.

Parameter  |  Target |  Result
--|---|--
X  | < 0.9  |  0.0677
Y  | < 0.10  |  0.0844
VX  | < 0.40  |  0.3450
VY  | < 0.30  |  0.2356

Therefore the solution acheives the required performance.


A screenshot can be seen below:
![Simulator View](https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/writeup/simulator%20_screenshot.png  "Simulator View")

A zoomed in screen shot of the simulator, showing the UKF tracking the vehicle well in a turn. The position output by the UKF is shown as green triangles.

![Simulator View](https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/writeup/sim_zoomed_in.png  "Simulator View Zoomed")


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

The implementation can be modified to use radar or lidar only by modifying the parameters use_laser_ and use_radar_  below:
```
// if this is false, laser measurements will be ignored (except during init)
use_laser_ = true;

// if this is false, radar measurements will be ignored (except during init)
use_radar_ = true;
```

## NIS Visulations

The NIS for the LIDAR and RADAR was visualised.
In order to perform this, the UKF.cpp stores the calculated NIS values in 2 log files. These log files are then parsed and visualised by the python file [nis_viz.py][e09286c2]

  [e09286c2]: https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/nis/nis_viz.py "nis_viz.py"

The visualisations of the NIS for LIDAR and RADAR are below.

![NIS LIDAR](https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/nis/NIS_plot_lidar.png)
![NIS RADAR](https://github.com/Geordio/CarND-Unscented-Kalman-Filter-Project/blob/master/nis/NIS_plot_radar.png)

In both instances the majority of the data  points are below the 95% confience line as per the project objectives. There appears to be an issue with the initialistaion of the RADAR, as the NIS value is much higher than expected, however the remianing points are all within the expected range.

## Code Efficency

I have not fully optimised the code yet I planned to implement a method to contain the common functionality of the LIDAR and RADAR update methods, but as yet I have not done this.
There is further optimisation that can be done, such as by removing the repeated calculations of the number of sigma points (an easy fix)
