import numpy as np
import skimage
import skimage.io
import matplotlib.pyplot as plt

image = skimage.io.imread('./13901.tif')

print('Image 1')
print(image)
print(type(image))
print(image.shape)

plt.imshow(image, cmap='gray')
plt.show()
print(image[0][0])

image[0, 0] = 2
print('Image 2')
print(image)
print('Image 3')
print(image[400:530, 400:600])
cropped = image[400:530, 400:600].copy()
plt.imshow(cropped)
plt.show()
print(cropped.shape)
print(image[400:530, :].shape)
print(image[400:, :].shape)

print(np.zeros(shape=(5, 3)))
print(np.ones(shape=(5, 3)))
print(np.arange(start=4, stop=12, step=2))
print(np.random.poisson(lam=3, size=(3, 5)))
cropped_plus_three = cropped + 3
print('Image 4')
print(cropped_plus_three)
print(cropped)
print(cropped * 3)
print(cropped / 3)
print(cropped - 3)
print(cropped ** 2)

#  NUMPY HWERE
print('NUMBEE')
print(np.cos(cropped))
print(np.max(cropped))
print(np.min(cropped))
print(np.mean(cropped))
print(np.std(cropped))
print(cropped.shape)
noise_image = np.random.poisson(lam=3, size=cropped.shape)
print(noise_image)
corrupted = cropped + 100 * noise_image
plt.imshow(cropped, cmap='gray')
plt.show()
plt.imshow(corrupted, cmap='gray')
plt.show()
print(cropped > 450)
array_bool = cropped > 450
plt.imshow(array_bool, cmap='gray')
plt.show()
plt.imshow(cropped, cmap='gray')
plt.show()