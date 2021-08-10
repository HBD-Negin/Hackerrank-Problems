arr = list(map(int , input().split(" ")))

min_val = min(arr)
max_val = max(arr)
sum_val = sum(arr)

print(sum_val-max_val, sum_val-min_val)