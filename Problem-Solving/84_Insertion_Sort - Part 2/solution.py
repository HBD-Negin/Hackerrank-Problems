arlen = int(input())
temp_ar = input().split()
ar = []
for a in temp_ar:
    ar.append(int(a))
i = 1
switch = False
while(i < len(ar)):
    j = i
    switch = False
    while(ar[j] < ar[j-1] and j > 0):
        ar[j], ar[j-1] = ar[j-1], ar[j]
        switch = True
        j -= 1
    i += 1
    for num in ar:
        print(num,'',end='')
        if ar.index(num) == len(ar)-1:
            print()