n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

pears = 0
color = set()

for i in range(len(ar)):
    if ar[i] not in color:
        color.add(ar[i])
    else:
        pears += 1 
        color.remove(ar[i])

result = pears

print(result)
