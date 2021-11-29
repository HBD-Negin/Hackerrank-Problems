n = int(input())
lengths = list(map(int, input().split()))
print(n)
shortest = min(lengths)
lengths = list(filter((shortest).__ne__, lengths))
while True:
    new = []
    for i in lengths:
        if (i-shortest) > 0:
            new.append(i-shortest)
    lengths = new
    if len(lengths) > 0:
        shortest = min(lengths)
    else:
        break
    print(len(lengths))
    lengths = list(filter((shortest).__ne__, lengths))
