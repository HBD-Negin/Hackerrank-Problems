n = int(input())
clouds = list(map(int, input().split()))
steps = 0
current_pos = 0
if n > 2:
    while True:
        if clouds[current_pos+2] == 1:
            current_pos += 1
        else:
            current_pos += 2
        steps += 1
        if current_pos >= n-3:
            if n > 3:
                steps += 1
            break
    print(steps)
else:
    if n <= 1:
        print(0)
    else:
        print(1)
