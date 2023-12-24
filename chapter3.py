import matplotlib.pyplot as plt
import numpy as np

plt.imshow(np.random.randint(0, 255, (10, 10)));
plt.show()

fig, ax = plt.subplots()
plt.show()

fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(np.random.randint(0, 255, (10, 10)))
ax.set_xlabel('my label')
plt.show()

import skimage.io

image = skimage.io.imread('./13901.tif')
print(image.shape)

image_rgb = skimage.io.imread('./46658_784_B12_1.tif')
print(image_rgb.shape)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(image_rgb)
plt.show()

# Channel 1 RED
image_channel1 = image_rgb[:, :, 0]
plt.imshow(image_channel1)
plt.show()
# Channel 2 BLue
image_channel2 = image_rgb[:, :, 1]
plt.imshow(image_channel2)
plt.show()
# Channel 3 GReen
image_channel3 = image_rgb[:, :, 2]
plt.imshow(image_channel3)
plt.show()

# HISTOGRAM Image
print(image_channel1.shape)
print(image_channel1.ravel().shape)
plt.hist(image_channel1.ravel())
plt.show()

# TYPES OF IMG
print(image_channel1.max())
print(image_channel1.dtype)

# SHOW IMAGE
print(image_channel1[0:3, 0:3])
# DROP 10 PER IMAGE
print(image_channel1[0:3, 0:3] - 10)
# ESTIMATE 30 IMAGE
print(image_channel1[0:3, 0:3] - 30)
# SHOW
print(plt.imshow(image_channel1 - 30))

image_channel1_float = image_channel1.astype(np.float16)
print(image_channel1_float[0:3, 0:3])
print(image_channel1_float[0:3, 0:3] - 30)