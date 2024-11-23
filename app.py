import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Compute the Mandelbrot set.
    :param c: Complex number
    :param max_iter: Maximum number of iterations
    :return: Number of iterations before divergence or max_iter
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Generate the Mandelbrot set for the given dimensions.
    :param xmin, xmax, ymin, ymax: Viewport bounds
    :param width, height: Resolution of the output image
    :param max_iter: Maximum iterations
    :return: 2D numpy array representing the Mandelbrot set
    """
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    mandelbrot_vectorized = np.vectorize(mandelbrot, otypes=[np.int32])
    return mandelbrot_vectorized(C, max_iter)

def plot_mandelbrot(xmin, xmax, ymin, ymax, width=1000, height=1000, max_iter=100):
    """
    Plot the Mandelbrot set using the given parameters.
    :param xmin, xmax, ymin, ymax: Viewport bounds
    :param width, height: Resolution of the output image
    :param max_iter: Maximum iterations
    """
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.colorbar(label="Number of Iterations")
    plt.title(f"Mandelbrot Set (x=[{xmin}, {xmax}], y=[{ymin}, {ymax}])")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

# Interactive Zoom Function
def zoom_mandelbrot():
    """
    Allow user-defined zoom on the Mandelbrot set.
    """
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    zoom_level = 1
    while True:
        print(f"Current Zoom Level: {zoom_level}x")
        print(f"Viewport: x=[{xmin}, {xmax}], y=[{ymin}, {ymax}]")
        plot_mandelbrot(xmin, xmax, ymin, ymax, max_iter=300)
        
        try:
            zoom_factor = float(input("Enter zoom factor (e.g., 2 for 2x zoom, -1 to quit): "))
            if zoom_factor == -1:
                break
            
            x_center = float(input("Enter x-coordinate of zoom center (default 0): ") or 0)
            y_center = float(input("Enter y-coordinate of zoom center (default 0): ") or 0)
            
            x_width = (xmax - xmin) / zoom_factor
            y_width = (ymax - ymin) / zoom_factor
            
            xmin = x_center - x_width / 2
            xmax = x_center + x_width / 2
            ymin = y_center - y_width / 2
            ymax = y_center + y_width / 2
            
            zoom_level *= zoom_factor
        except ValueError:
            print("Invalid input. Please try again.")
            continue

if __name__ == "__main__":
    zoom_mandelbrot()
