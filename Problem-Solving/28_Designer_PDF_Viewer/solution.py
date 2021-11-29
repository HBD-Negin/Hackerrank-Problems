heights = list(map(int, input().split()))
word = input()
width = len(word)
height = 0
for i in word:
    temp = heights[(ord(i)-97)]
    if temp > height:
        height = temp
print(height*width)
