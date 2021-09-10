def reverse(n):
    num = str(n)
    return int(num[::-1])

i, j, k = map(int, input().split())
count = 0
for a in range(i, j+1):
    temp = abs(a-reverse(a))
    if temp % k == 0:
        count += 1
print(count)
