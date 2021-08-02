n = int(input())

matrix = []

# Reading matrix
for i in range(n):
  line = list(map(int, input().split()))
  matrix.append(line)

sumOfPrimary = 0
sumOfSecondary = 0

# Finding diagonal sums
for i in range(n):
  sumOfPrimary += matrix[i][i]
  sumOfSecondary += matrix[i][n-i-1]

print(abs(sumOfPrimary - sumOfSecondary))