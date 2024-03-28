def gcd(a, b):

  (a, b) = (min(a, b), max(a, b))
  assert a >= 0 and b > 0

  if a == b:
    return b
  else:
    while a > 0:
      # a < b here.
      # "%" is the "mod" operator in Python.
      (a, b) = (b % a, a)
      # Now a < b again.
    return b

if __name__ == "__main__":
  a = int(input("Enter a, the first integer of two: "))
  b = int(input("Enter b, the second integer of two: "))

  g = gcd(a, b)
  print("The gcd of", a, "and", b, "is", g)
