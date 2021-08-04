# Reading inputs
n = int(input())
arr = list(map(int, input().split()))

countZeroes = 0
countPositive = 0
countNegative = 0

for number in arr:
  if number == 0:
    countZeroes += 1
  elif number > 0:
    countPositive += 1
  else:
    countNegative += 1

ratioOfPositives = countPositive / n
ratioOfNegatives = countNegative / n
ratioOfZeroes = countZeroes / n

print("%.6f" % ratioOfPositives)
print("%.6f" % ratioOfNegatives)
print("%.6f" % ratioOfZeroes)