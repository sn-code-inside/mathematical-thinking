def sqrt_by_binary_search(c, epsilon):

  assert c > 1
  assert epsilon > 0

  i = 0
  low = 1.0
  high = c
  midpoint = (low + high) / 2.0
  print("Initial midpoint =", midpoint)
  
  # Repeat forever.
  while True:
  
    i = i + 1
    square = midpoint * midpoint
    error_bound = high - low
    print("i =", i, ": low =", low, ", high =", high, ", midpoint =", midpoint, ", and error_bound =", error_bound)
    if error_bound <= epsilon:
      # The next line causes the program to exit the loop.
      print("Breaking.")
      break
  
    else: 
      if square == c:
        return midpoint, 0, i
      if square > c:
        # midpoint is too large to be the square root. 
        # The square root is between low and midpoint, so
        # replace the interval [low, high] by the interval [low, midpoint],
        # that is, replace high by midpoint.
        high = midpoint
      else: # square < c
        # midpoint is too small to be the square root. 
        # The square root is between midpoint and high,
        # so replace the interval [low, high] by the interval [midpoint, high],  
        # that is, replace low by midpoint.
        low = midpoint
    
    # Calculate the new midpoint of low and high.
    midpoint = (low + high) / 2.0

  # high - low is an upper bound on the difference between midpoint and the true square root.
  return midpoint, high - low, i

if __name__ == "__main__":
  c = float(input("Enter c: "))
  epsilon = float(input("Enter epsilon: "))
  # If epsilon is too small relative to c, the code might run forever.
  
  sqrt_c, error_bound, iteration_count = sqrt_by_binary_search(c, epsilon)
  print("Final result is ", sqrt_c, "with error_bound =", error_bound, \
    "after", iteration_count, "iterations.")   
