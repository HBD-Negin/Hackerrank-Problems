import math
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    count = int(math.floor(b**0.5))-int(math.ceil(a**0.5))+1
    print(count)