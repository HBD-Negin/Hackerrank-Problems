arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

count = [0] * 6
for i in arr:
    count[i] += 1
    
result = count.index(max(count))

print(result)
