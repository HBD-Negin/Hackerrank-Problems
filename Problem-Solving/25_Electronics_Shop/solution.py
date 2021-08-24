s, n, m = map(int, input().split())
keyboardPrices = list(map(int, input().split()))
usbPrices = list(map(int, input().split()))
big = 0
for i in keyboardPrices:
    for j in usbPrices:
        if i+j > big and i+j <= s:
            big = i+j
if big == 0:
    print(-1)
else:
    print(big)