import random
from PIL import Image, ImageDraw

def fire(i, b, r, B):
  # Additive increase
  r[i] += 1.0
  # Send data.
  b = min(b + r[i], B)
  # If the buffer is full, source i "backs off" (multiplicative decrease).
  if b == B: 
    r[i] /= 2.0
  return b, r

def run_one_step(b, r, B, d):
  # The buffer is partially drained.
  b = max(b - d, 0)

  # Randomly decide who fires first.
  rand = random.random() 
  i = 0 if rand < 0.5 else 1

  # Source i in {0, 1} fires first.
  b, r = fire(i, b, r, B)
  # Source 1 - i fires next.
  b, r = fire(1 - i, b, r, B)
  return b, r

if __name__ == "__main__":

  B = float(input("Enter buffer size B: ")) # A good value is 4.0.
  # Start with a full buffer.
  b = B
  d = float(input("Enter the drain rate d: ")) # A good value is 3.0.
  r = [1.0, 1.0] # initial rates
  # A good value for num_time_steps is 1000000.
  num_time_steps = int(input("Enter the number of time steps: ")) 
  
  min_x = min_y = 1.0
  max_x = max_y = d
  
  width_in_pixels = height_in_pixels = 1000 
  # (255, 255, 255) means white background.
  image = Image.new('RGB', (width_in_pixels, height_in_pixels), (255, 255, 255))
  draw = ImageDraw.Draw(image)
  
  for step in range(num_time_steps): 

    b, r = run_one_step(b, r, B, d);

    # These are the x plot upper bound and the y plot upper bound.
    xplotub = 1000; yplotub = 1000
    if min_x <= r[0] <= xplotub and min_y <= r[1] <= yplotub:
      transformed_r0 = (r[0] - min_x) * (width_in_pixels) / (max_x - min_x)
      # Without the "height_in_pixels -" part, 
      # small values of r[1] would be near the top.
      transformed_r1 = \
        height_in_pixels - (r[1] - min_y) * (height_in_pixels) / (max_y - min_y)
      # (0, 0, 0) means black.
      draw.point([transformed_r0, transformed_r1], (0, 0, 0)) 
    
  image.save('tcp_output.png', 'PNG')
