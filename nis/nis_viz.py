import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

radarIndex = np.loadtxt(open("radarNIS.csv", "rb"), usecols=[0], delimiter=",", skiprows=1)
radarNis = np.loadtxt(open("radarNIS.csv", "rb"), usecols=[1],delimiter=",", skiprows=1)

lidarIndex = np.loadtxt(open("lidarNIS.csv", "rb"), usecols=[0], delimiter=",", skiprows=1)
lidarNis = np.loadtxt(open("lidarNIS.csv", "rb"), usecols=[1], delimiter=",", skiprows=1)


print ("Lidar NIS: {}" .format(lidarNis))
print ("Radar NIS: {}" .format(radarNis))

#for the parmters and consistency lesson, the 95% values
radar95line = 7.815
lidar95line = 5.991


plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)

plt.plot(radarIndex, radarNis, color="b", linewidth=1.0, linestyle="-")
plt.axhline( y=radar95line, color='r', linestyle='-', label='threshold' )
plt.title('Radar NIS')
plt.savefig( "NIS_plot_radar.png", bbox_inches = 'tight')
plt.show()


plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)

plt.plot(lidarIndex, lidarNis, color="b", linewidth=1.0, linestyle="-")
plt.axhline( y=lidar95line, color='r', linestyle='-', label='threshold' )
plt.title('Lidar NIS')

plt.savefig( "NIS_plot_lidar.png", bbox_inches = 'tight')
plt.show()


