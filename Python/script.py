import matplotlib.pyplot as plt 
import numpy as np
import random,string

#// Bias visualisation / Random points / Colors
def genpoints(num_points=4, limit=10):
    points= [(random.randint(1, limit), random.randint(1, limit)) for i in range (num_points)]
    return points