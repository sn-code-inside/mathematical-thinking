from PIL import Image, ImageDraw
from mandelbrot_module import mandelbrot

if __name__ == "__main__":

  # The plotting window goes from smallest_real to
  # largest_real on the x-axis and from smallest_imaginary
  # to largest_imaginary on the y-axis.
  smallest_real = -1.5
  largest_real = 0.68
  smallest_imaginary = -1.2
  largest_imaginary = 1.2
  
  # Break the x-range into scale_factor pieces.
  scale_factor = 300
  width_in_pixels = int(scale_factor * (largest_real - smallest_real))
  # Do the same for the y-range.
  height_in_pixels = int(scale_factor * (largest_imaginary - smallest_imaginary))
  
  # (0, 0, 0) means black background
  image = Image.new('RGB', (width_in_pixels, height_in_pixels), (0, 0, 0)) 
  draw = ImageDraw.Draw(image)
  
  # Let x vary from 0 to width_in_pixels - 1.
  for x in range(width_in_pixels):
    # Let y vary from 0 to height_in_pixels - 1.
    for y in range(height_in_pixels):
      # Convert pixel coordinates to a complex number with real part 
      # between smallest_real and largest_real and with
      # imaginary part between smallest_imaginary and largest_imaginary.
      real_part = smallest_real + (x / width_in_pixels) * \
        (largest_real - smallest_real)
      imaginary_part = smallest_imaginary + (y / height_in_pixels) * \
        (largest_imaginary - smallest_imaginary)
      c = complex(real_part, imaginary_part)
      color_vector = mandelbrot(c)
      # Plot the point (x, y) with the given color_vector.
      draw.point([x, y], color_vector)
  
  image.save('mandelbrot_output.png', 'PNG')
