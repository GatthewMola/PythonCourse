import numpy as np
from PIL import Image

# Create 3D numpy array of zeros, then replaces zeros (black pixels) with yellow pixels
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# Make a red patch (row)
data[1:3] = [255, 0, 0]

# Make a red patch (column)
data[:, 1:3] = [255, 0, 0]

# Make a red patch (square in the middle)
data[1:3, 1:3] = [255, 0, 0]

# Make a red patch (square in the top-left corner)
data[0:3, 0:2] = [255, 0, 0]

# Making more shapes within the canvas
data[0:3, 0:2] = [255, 0, 0]
data[3:4, 1:4] = [225, 230, 55]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')