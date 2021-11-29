t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in str(n):
        if int(j) != 0:
            if n%int(j) == 0:
                count += 1
    print(count)