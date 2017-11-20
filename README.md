# Unscented Kalman Filter Project Starter Code
Self-Driving Car Engineer Nanodegree Program

This document describes my solution for the Udacity Unscented Kalman Filter project in term 2 of the SDC nano degree


## Compiling

The project can be compiled by execting 'make' in the build directory

## Accuracy

  [f652f87d]: test "test"

When run against the simulator using Dataset 1, my implementation acheives a final RMSE of:
X: 0.0973
Y: 0.0855
VX: 0.4513
VY: 0.4399

A screenshot can be seen below:
![Simulator View](https://github.com/Geordio/CarND--Kalman-Filter-Project/blob/master/simulator_screenshot.png  "Simulator View")

This satisifies the required target of 0.11, .11, 0.52, 0.52 respectively.

## Processing Flow

My implementation follows the general processing flow (as per the project skeleton code) of:
- Initialisation. Including initialisation of the state vectors from the first measurements
- Prediction
- Update
	- For RADAR calculate the Jacobian and call the Update Extended Kalman Filter, which converts from Polar coordinates.
	- For LIDAR call the Update Kalman Filter

Below are the main files updated:

1. kalman_filter.cpp. Completed the Update and UpdateEKF methods
2. FusionEKF.cpp. Populated initialisation, prediction and basic update flow.
3. tools.cpp. Added the body to the RMSE and Jacobian methods


## NIS Visulations

The NIS for the LIDAR and RADAR was visualised.
In order to perform this, the UKF.cpp stores the calculated NIS values in 2 log files. These log files are then parsed and visualised by the python file

## Code Efficency

I have not fully optimised the code yet I planned to implement a method to contain the common functionality of the Update and UpdateEKF methods, but as yet I have not done this.
