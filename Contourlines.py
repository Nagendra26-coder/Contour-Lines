import numpy as np
import matplotlib.pyplot as plt

#Generate some sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
z = np.sin(np.sqrt(X**2 + Y**2))

#Create the Contour Plot
plt.contour(x,y,z, levels=10, cmap='RdYlBu')
plt.colorbar()

#show the plot
plt.show()
