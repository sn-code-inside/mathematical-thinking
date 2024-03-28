import math

def sqrt_by_newtons_method(c, epsilon): 
  assert c > 1
  assert epsilon > 0
  x = c
  i = 0
  pseudoerror = abs(x * x - c)
  # (Instead, we could terminate when consecutive approximations differ by < epsilon.)
  while pseudoerror >= epsilon:
    i = i + 1
    x = (x + c / x) / 2.0
    pseudoerror = abs(x * x - c)
    print("\nActual error, unused by the code, is", abs(x - math.sqrt(c)))
    print("i =", i, ",  x = ", x, ", and pseudoerror =", pseudoerror)
  return x, pseudoerror, i

if __name__ == "__main__":
  c = float(input("Enter c: "))
  epsilon = float(input("Enter epsilon: "))
  # If epsilon is too small relative to c, the code might run forever.
   
  sqrt_c, pseudoerror, iteration_count = sqrt_by_newtons_method(c, epsilon)
  print("\nFinal result is ", sqrt_c, "with pseudoerror =", pseudoerror, \
    "after", iteration_count, "iterations.")   
