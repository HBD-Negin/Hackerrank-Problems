t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for j in a:
        if j <= 0:
            count += 1
    if count < k:
        print("YES")
    else:
        print("NO")
