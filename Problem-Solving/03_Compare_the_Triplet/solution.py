a1, a2, a3 = map(int, input().split(" "))
b1, b2, b3 = map(int, input().split(" "))

pa = 0
pb = 0

if a1 > b1:
  pa += 1
elif b1 > a1:
  pb += 1

if a2 > b2:
  pa += 1
elif b2 > a2:
  pb += 1

if a3 > b3:
  pa += 1
elif b3 > a3:
  pb += 1

print(pa, pb)