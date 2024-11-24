import matplotlib.pyplot as plt
import numpy as np
import random, string

# Generate random bias points
def generate_random_points(num_points=4, limit=10):
    points = [(random.randint(1, limit), random.randint(1, limit)) for _ in range(num_points)]
    return points

# Number of bias-counterbias pairs (random between 4 and 26)
num_pairs = random.randint(4, 26)

#Generate random bias points
bias_points = generate_random_points(num_pairs)

#// Extract bias and counter-bias points
bias_x, bias_y = zip(*bias_points)
counter_bias_x = [-x for x in bias_x]
counter_bias_y = [-y for y in bias_y]

#// Plot the diagram
plt.figure(figsize=(10, 10))
plt.axhline(0, color='black', linewidth=0.5)  # Horizontal axis
plt.axvline(0, color='black', linewidth=0.5)  # Vertical axis

#// Add grid
plt.grid(color='gray', linestyle='--', linewidth=0.5)

#// Plot lines connecting biases to counter-biases with labels
for i, (x, y, cx, cy) in enumerate(zip(bias_x, bias_y, counter_bias_x, counter_bias_y)):
    label = string.ascii_uppercase[i] if i < 26 else f"A{i}"  # Generate labels
    color = [random.random() for _ in range(3)]  # Random color
    plt.plot([x, cx], [y, cy], linestyle='-', color=color, alpha=0.7, label=f"Line {label}")
    
    #// Letters at 90% distance along the line 
    text_x = x + (cx - x) * 0.90
    text_y = y + (cy - y) * 0.90
    plt.text(text_x, text_y, label, color=color, fontsize=9, fontweight='bold', ha='center', va='center')

#// Plot bias and counter-bias points
plt.scatter(bias_x, bias_y, color='blue', label='Bias Points')
plt.scatter(counter_bias_x, counter_bias_y, color='red', label='Counter-Bias Points')

#//Set axis limits and labels
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Randomized Bias Visualization")
plt.legend()

#// Make a png to show the BIAS Visualisation as an image file
plt.savefig("bias_pics/bias_visual.png")
plt.show()
#// Pic saved to bias_pics folder