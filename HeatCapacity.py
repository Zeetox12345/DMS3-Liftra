import numpy as np
import matplotlib.pyplot as plt

def steel_heat_capacity(theta):
    """Returns specific heat capacity ca [J/kgK] for steel at temperature theta [°C]."""
    ca = np.zeros_like(theta, dtype=float)
    # For 20°C ≤ θa < 600°C
    mask1 = (theta >= 20) & (theta < 600)
    ca[mask1] = (
        425
        + 7.73e-1 * theta[mask1]
        - 1.69e-3 * theta[mask1] ** 2
        + 2.22e-6 * theta[mask1] ** 3
    )
    # For 600°C ≤ θa < 735°C
    mask2 = (theta >= 600) & (theta < 735)
    ca[mask2] = 666 + 13002 / (738 - theta[mask2])
    # For 735°C ≤ θa < 900°C
    mask3 = (theta >= 735) & (theta < 900)
    ca[mask3] = 545 + 17820 / (theta[mask3] - 731)
    # For 900°C ≤ θa ≤ 1200°C
    mask4 = (theta >= 900) & (theta <= 1200)
    ca[mask4] = 650
    # For theta < 20°C, extrapolate as constant
    ca[theta < 20] = ca[mask1][0] if np.any(mask1) else 425
    return ca

def steel_thermal_conductivity(theta):
    """Returns thermal conductivity lambda_a [W/mK] for steel at temperature theta [°C] (DS/EN-1993-2-1)."""
    la = np.zeros_like(theta, dtype=float)
    # For 20°C ≤ θa < 800°C
    mask1 = (theta >= 20) & (theta < 800)
    la[mask1] = 54 - 3.33e-2 * theta[mask1]
    # For 800°C ≤ θa ≤ 1200°C
    mask2 = (theta >= 800) & (theta <= 1200)
    la[mask2] = 27.3
    # For theta < 20°C, extrapolate as constant
    la[theta < 20] = la[mask1][0] if np.any(mask1) else 54
    return la

# Extracted data points in the interval 0-1200°C with 10°C resolution
theta_points = np.arange(0, 1201, 10)
ca_points = steel_heat_capacity(theta_points)
la_points = steel_thermal_conductivity(theta_points)

# ...existing code...

# Save temperature and thermal conductivity to a text file in the specified directory
output_path = r"C:\Users\atbys\Thermal\ThermalDataInter.txt"
output_data = np.column_stack((theta_points, la_points))
np.savetxt(output_path, output_data, fmt="%.1f\t%.4f", header="Temperature[°C]\tThermalConductivity[W/mK]", comments='')

# ...existing code...
# ...existing code...
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(theta_points, ca_points, marker='o', label="Specific Heat Capacity $c_a$")
plt.xlabel("Temperature $\\theta_a$ [°C]")
plt.ylabel("Specific Heat Capacity $c_a$ [J/kgK]")
plt.title("Specific Heat Capacity of Steel vs Temperature")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(theta_points, la_points, marker='s', color='orange', label="Thermal Conductivity $\\lambda_a$")
plt.xlabel("Temperature $\\theta_a$ [°C]")
plt.ylabel("Thermal Conductivity $\\lambda_a$ [W/mK]")
plt.title("Thermal Conductivity of Steel vs Temperature (DS/EN-1993-2-1)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

