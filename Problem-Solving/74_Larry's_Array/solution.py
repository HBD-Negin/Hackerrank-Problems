def canSort(l):
    s = sorted(l)
    for i in s[:-2]:
        if l.index(i) % 2:
            l.remove(i)
            l[0],l[1]=l[1],l[0]
        else:
            l.remove(i)
    if l[0]<l[1]:
        return True
    else:
        return False

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    A = list(map(int, input().split()))
    if canSort(A):
        print("YES")
    else:
        print("NO")
