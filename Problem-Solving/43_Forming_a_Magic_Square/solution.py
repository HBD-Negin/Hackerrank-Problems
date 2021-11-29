def getCost(array, magic):
  cost = 0
  cost += (abs(array[0][0] - magic[0][0]) + abs(array[0][1] - magic[0][1]) + abs(array[0][2] - magic[0][2]))
  cost += (abs(array[1][0] - magic[1][0]) + abs(array[1][1] - magic[1][1]) + abs(array[1][2] - magic[1][2]))
  cost += (abs(array[2][0] - magic[2][0]) + abs(array[2][1] - magic[2][1]) + abs(array[2][2] - magic[2][2]))
  return cost

array = []
array.append(list(map(int, input().split())))
array.append(list(map(int, input().split())))
array.append(list(map(int, input().split())))

all_magic_arrays = [
  [[8,1,6], [3,5,7], [4,9,2]],
  [[6,7,2], [1,5,9], [8,3,4]],
  [[2,9,4], [7,5,3], [6,1,8]],
  [[4,3,8], [9,5,1], [2,7,6]],
  [[6,1,8], [7,5,3], [2,9,4]],
  [[2,7,6], [9,5,1], [4,3,8]],
  [[4,9,2], [3,5,7], [8,1,6]],
  [[8,3,4], [1,5,9], [6,7,2]]
]

costs = []
for ma in all_magic_arrays:
  costs.append(getCost(array, ma))

print(min(costs))