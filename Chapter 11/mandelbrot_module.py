from PIL import Image, ImageDraw

def mandelbrot(c):
  num_iterations = 100
  threshold = 10
  z = complex(0, 0)
  # The next statement runs for n = 1, 2, 3, ..., num_iterations.
  for n in range(1, 1 + num_iterations):
    z = z * z + c
    if abs(z) > threshold: return (0, 0, 255) # Not in Mandelbrot set so blue.
  return (255, 0, 0) # In Mandelbrot set so red.
