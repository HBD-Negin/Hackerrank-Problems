t = int(input())
for i in range(t):
    n, m, s = map(int, input().split())
    shift = (m+s-1)%n
    if shift == 0:
        shift = n
    print(shift)