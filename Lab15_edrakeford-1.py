"""
Program Name: Lab15_edrakeford-1.py

Author: Elijah Drakeford

Purpose: This program uses matplotlib to plot a rose curve 
and displays the plot in an image file

Starter Code: None

Date: May 3, 2026
"""

import matplotlib.pyplot as plt
import math

# list for x and y
x_values = []
y_values = []

# For rose curve
n = 5

# making function
theta = 0
while theta <= 2 * math.pi:
    r = math.cos(n * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    x_values.append(x)
    y_values.append(y)

    theta += 0.01

# Plot
plt.plot(x_values, y_values)

# Add title and labels
plt.title("Rose Curve")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()