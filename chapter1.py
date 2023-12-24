import skimage
import matplotlib.pyplot as plt

a = 3
print(a)

b = 5
c = 2
print(a + b)

d = a + b
print(d)

a = 100
print(a)

d = a + b
print(d)

my_text = 'This is my text'
print(my_text)

my_list = [3, 8, 5, 9]
print(my_list)


def my_fun(x, a, b):
    out = a * x + b
    return out


print(my_fun(3, 2, 5))

my_text = 'This is my text'
print(len(my_text))

print(my_text.lower())

a = 3 + 5j
print(a.real)

my_address = './19838_1252_F8_1.tif'
print(skimage.io.imread(my_address))

image = skimage.io.imread(my_address)
plt.imshow(image, cmap='gray')
plt.show()