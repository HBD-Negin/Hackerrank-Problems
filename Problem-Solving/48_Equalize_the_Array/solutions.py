n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

result = (len(arr) - arr.count(max(set(arr), key = arr.count)))

print(result)