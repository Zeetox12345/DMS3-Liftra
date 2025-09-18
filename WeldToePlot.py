# Plotting Tool for Ansys Temperature Tabular Data Output
import matplotlib.pyplot as plt
import numpy as np

data_path = "C:\\Users\\atbys\\Desktop\\Ansys\\ModelV3\\HeatDist.txt"
time, min_temp, max_temp, avg_temp = np.loadtxt(data_path,unpack=True)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Min and Avg Temp
axes[0].plot(time, min_temp, label="Min Temp")
axes[0].plot(time, avg_temp, label="Avg Temp")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Temperature [C]")
axes[0].set_title("Min and Avg Temperature vs Time")
axes[0].legend()
axes[0].grid(True)

# Second subplot: Max Temp
axes[1].plot(time, max_temp, color='r', label="Max Temp")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Temperature [C]")
axes[1].set_title("Max Temperature vs Time")
axes[1].legend()
axes[1].grid(True)

# Add a common subtitle below the main titles
fig.suptitle("FEA Model Setup", fontsize=10, y=0.97)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for suptitle
plt.show()

