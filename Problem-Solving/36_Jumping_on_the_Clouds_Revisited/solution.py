n, k = map(int, input().split())
clouds = list(map(int, input().split()))
e = 100
pos = 0
while True:
    pos = (pos+k)%n
    if clouds[pos] == 1:
        e -= 3
    else:
        e -= 1
    if pos == 0:
        break
print(e)