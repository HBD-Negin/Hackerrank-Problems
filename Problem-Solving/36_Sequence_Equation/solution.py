n = int(input())
p = list(map(int, input().split()))
for i in range(1, n+1):
    a = p.index(i)+1
    a = p.index(a)+1
    print(a)