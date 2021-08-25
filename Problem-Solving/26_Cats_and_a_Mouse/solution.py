q = int(input())
for i in range(q):
    a, b, c = map(int, input().split())
    d1 = abs(a-c)
    d2 = abs(b-c)
    if d1 > d2:
        print("Cat B")
    elif d2 > d1:
        print("Cat A")
    else:
        print("Mouse C")