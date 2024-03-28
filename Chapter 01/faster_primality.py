import sys
import math

def is_prime(n):
  # Check that n is an integer at least 2.
  assert int(n) == n and n >= 2.

  s = int(math.sqrt(n))
  # Check potential divisors between 2 and s, including both 2 and s.
  print("Checking potential divisors between 2 and", s)
  for d in range(2, s + 1):
    # n % d is the remainder when dividing n by d.
    if n % d == 0:
      # Return a list containing False and the divisor.
      return [False, d]
  # Return a list containing only True.
  return [True]

# This is the main program.
if __name__ == "__main__":
  n_string = input("Please enter an integer >= 2 which you want to check for primality: ")
  # Convert the string to an integer.
  n = int(n_string)
  result = is_prime(n)
  if result[0]:  
    print(n, "is prime.")
  else:
    print(n, "is not prime because", result[1], "divides", n)
