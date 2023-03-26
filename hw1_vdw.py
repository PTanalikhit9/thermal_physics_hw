
import matplotlib.pyplot as plt

# Data points
data = [(100, -.00016), (200, -.000035), (300, -.0000042), (400, .000009), (500, .0000169), (600, .0000213)]

# Function for van der Waals equation
def vdw(t):
    return .00003 - .1 / (8.315 * t)

# Separate data points into x and y coordinates
x_data, y_data = zip(*data)

# Plot data points
plt.scatter(x_data, y_data, label='data', color='blue')

# Plot van der Waals equation
t = [i for i in range(100, 601)]
vdw_values = [vdw(t_val) for t_val in t]
plt.plot(t, vdw_values, label='vdw', color='red')

# Set plot range
plt.xlim(0, 600)
plt.ylim(min(y_data), max(y_data))

# Show the plot
plt.legend()
plt.show()
