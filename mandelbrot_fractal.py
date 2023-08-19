import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n


def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = np.vectorize(mandelbrot)(Z, max_iter)
    return C


width = 800
height = 800
x_min, x_max = -2.5, 1.5
y_min, y_max = -2, 2
max_iter = 1000

mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)

plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_image, extent=(x_min, x_max, y_min, y_max), cmap='inferno', interpolation='bilinear')
plt.colorbar(label='Iterations')
plt.title('Mandelbrot Fractal')
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()
