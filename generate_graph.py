import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create the graph
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title('Movie Popularity')
plt.xlabel('Movies')
plt.ylabel('Titles')

# Save the graph as an image (e.g., sine_wave.png)
plt.savefig('sine_wave.png')
