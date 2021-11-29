valley = 0
lvl = 0
count = 0
n = int(input())
path = input()
for i in path:
    if i == 'U':
        lvl = lvl + 1
    else:
        lvl = lvl - 1
    if lvl < 0:
        if valley == 0:
            valley = 1
            count = count + 1
    else:
        if valley == 1:
            valley = 0
print(count)