T = int(input())
    
for _ in range(T):
  n = int(input())
  a = int(input())
  b = int(input())
  
  print(*sorted(set(x * a + (n - 1 - x) * b for x in range(n))))