#// Using Jupyter for viewing compilator for Java
import matplotlib.pyplot as plt 
import numpy as np
import random,string

#// Bias generate random points
def genpoints(num_points=4, limit=10):
    points= [(random.randint(1, limit), random.randint(1, limit)) for i in range (num_points)]
    return points

#// Num bias-counterb pairs (from 4-20 seems ok )
num_pairs = random.randint (4, 20)

#// Random Bias Points call
bias_points = genpoints(num_pairs)

#//Unpack the list (x and y)
bias_x, bias_y = zip(*bias_points)
counter_bias_x = [x for x in bias_x]
counter_bias_y = [y for y in bias_y]

#// Plotting the info in diagram
plt.figure(figsize=(10, 10))
plt.axhline(0, color="Black", linewidth = 0.5)
plt.axvline(0, color="Black", linewidth = 0.5)
