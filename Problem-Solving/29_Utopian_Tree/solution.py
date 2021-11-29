t = int(input())
for i in range(t):
    n = int(input())
    height = 1
    for j in range(1, n+1):
        if j%2 == 1:
            height *= 2
        else:
            height += 1
    print(height)
