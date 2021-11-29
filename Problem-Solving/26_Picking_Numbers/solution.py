from collections import Counter

def most_common(lst):
    data = Counter(lst)
    return max(lst, key=data.get)

n = int(input())
a = list(map(int, input().split()))
a.sort()
unique = list(set(a))
prev = unique[0]
big = a.count(most_common(a))
for i in range(1, len(unique)):
    if abs(prev-unique[i]) <= 1:
        temp = a.count(prev)+a.count(unique[i])
        if temp > big:
            big = temp
    prev = unique[i]
print(big)
