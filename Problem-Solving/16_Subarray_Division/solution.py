n = int(input().strip())
squares = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]

count = 0
for i in range(m, n+1):
    if sum(squares[i-m:i]) == d:
        count += 1
        
print(count)    