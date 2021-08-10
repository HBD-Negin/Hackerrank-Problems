n = input()
arr = list(map(int, input().split(" ")))

max_val = max(arr)
count = 0
for i in arr:
    if i == max_val:
        count += 1

print(count)