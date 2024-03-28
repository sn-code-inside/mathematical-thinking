from PIL import Image, ImageDraw
import math

def f(z):
  # f(z) = z^3 - 1.
  return z * z * z - 1.0

def fprime(z):
  # The slope (or derivative) of f(z) = z^3 - 1 is 3 z^2.
  return 3.0 * z * z

def julia(z, num_iterations, tol):
  # The three complex cube roots of 1.
  roots = [complex(1.0, 0.0), complex(-0.5, math.sqrt(3.0) / 2.0), 
    complex(-0.5, -math.sqrt(3.0) / 2.0)] 
  colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] # red, green, blue

  for i in range(num_iterations):
    # Check to see if z is close to a root.  If so, return
    # the color of that root.
    for j in range(len(roots)):
      if abs(z - roots[j]) <= tol: return colors[j]
    # No color found, so do a step of Newton iteration.
    deriv = fprime(z)
    if deriv == 0: 
      return (0, 0, 0) # black
    # Newton iteration.
    z = z - f(z) / deriv
  
  # If haven't converged yet, color the point black.
  return (0, 0, 0)

if __name__ == "__main__":
  # The plotting window goes from smallest_real to
  # largest_real on the x-axis and from smallest_imaginary
  # to largest_imaginary on the y-axis.
  smallest_real = -1.75 
  largest_real = 1.5 
  smallest_imaginary = -1.5 
  largest_imaginary = 1.5 
  
  scale_factor = 300
  width_in_pixels = int(scale_factor * (largest_real - smallest_real))
  height_in_pixels = int(scale_factor * (largest_imaginary - smallest_imaginary))
  
  image = Image.new('RGB', (width_in_pixels, height_in_pixels), (0, 0, 0))
  draw = ImageDraw.Draw(image)
  
  # Let ix vary from 0 to width_in_pixels - 1.
  for ix in range(width_in_pixels):
    # Let iy vary from 0 to height_in_pixels - 1.
    for iy in range(height_in_pixels):
      # Convert pixel coordinates to a complex number with real part x
      # between smallest_real and largest_real and with
      # imaginary part y between smallest_imaginary and largest_imaginary.
      x = smallest_real + (ix / width_in_pixels) * \
        (largest_real - smallest_real)
      y = smallest_imaginary + (iy / height_in_pixels) * \
        (largest_imaginary - smallest_imaginary)
      z = complex(x, y)
      color_vector = julia(z, 100, 0.000001)
  
      # Plot the point (ix, iy) with the given color_vector.
      draw.point([ix, iy], color_vector)
  
  image.save('julia_set_output3.png', 'PNG')
