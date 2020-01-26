# Your assignment is to calculate a sum of all even numbers of the Fibonacci sequence whose values do not
# exceed four million

def fibonacci(a, b) :
  outcome = 0
  while a + b < 4000000 :
    if ((a + b) % 2) == 0 :
      outcome += a + b
    a = b
    b = a + b
    print(a+b)

  return outcome

print(fibonacci(1, 1))