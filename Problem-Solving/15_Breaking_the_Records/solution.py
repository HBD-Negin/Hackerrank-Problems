size = int(input())
arr = [int(t) for t in input().strip().split()]

lo = arr[0]
hi = arr[0]

lob = 0
hib = 0

for i in range(1,len(arr)):
    if arr[i] < lo:
        lob += 1
        lo = arr[i]
    if arr[i] > hi:
        hib += 1
        hi = arr[i]

ans = [hib, lob]

print(str(ans)[1:-1].replace(",",""))
