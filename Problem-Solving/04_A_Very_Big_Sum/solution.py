ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result =0
for i in range(0,len(ar)):
    result += ar[i]

print(result)

