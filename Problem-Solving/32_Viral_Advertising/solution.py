n = int(input())
liked = 2
cum = 2
for i in range(n-1):
    liked = (liked*3)//2
    cum += liked
print(cum)
