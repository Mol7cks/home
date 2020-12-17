def collatz(n) -> int:
  if n == 1:
    return 1
  elif n%2 == 1:
    return 3*n+1
  else:
    return n/2
    
print(collatz(5))
