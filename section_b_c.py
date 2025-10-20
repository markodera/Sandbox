import math
import numpy as np
import matplotlib.pyplot as plt


# Constants
G = 6.674 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989 * 10**30  # Mass of the Sun (kg)

# Semi-major axis (in meters)
last_two_digits = 15
a_km = last_two_digits * 10**7  # Convert to km
a_m = a_km * 10**3  # Convert to meters

# Kepler's Third Law: T^2 = (4 * π^2 * a^3) / (G * M_sun)
T_squared = (4 * math.pi**2 * a_m**3) / (G * M_sun)

# Compute the orbital period (T) in seconds
T_seconds = math.sqrt(T_squared)

# Convert seconds to years
T_years = T_seconds / (60 * 60 * 24 * 365)

# Print results
print(f"Semi-major axis (a): {a_km} km")
print(f"Orbital period (T): {T_years:.2f} years")

# Define the ellipse parameters
a = a_m  # Semi-major axis in meters
e = 0.1  # Assume eccentricity (you can change this)
b = a * np.sqrt(1 - e**2)  # Semi-minor axis

# Generate points for the ellipse
theta = np.linspace(0, 2 * np.pi, 500)  # Angles from 0 to 360 degrees
x = a * np.cos(theta)  # X-coordinates
y = b * np.sin(theta)  # Y-coordinates

# Mark the perihelion and aphelion
perihelion = (a * (1 - e), 0)
aphelion = (a * (1 + e), 0)

# Plot the orbit
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Orbital Path")
plt.scatter(0, 0, color='orange', marker='o', label="Sun")  # Sun at the center
plt.scatter(*perihelion, color='red', label="Perihelion")
plt.scatter(*aphelion, color='blue', label="Aphelion")

# Labels and title
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Elliptical Orbit Simulation")
plt.legend()
plt.grid()
plt.axis("equal")  # Ensure equal aspect ratio
plt.show()