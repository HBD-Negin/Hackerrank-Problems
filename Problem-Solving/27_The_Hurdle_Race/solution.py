n, k = map(int, input().split())
heights = list(map(int, input().split()))
dose = 0
for i in heights:
    if i > k:
        dose += (i-k)
        k = i
print(dose)