first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

billed = b - (sum(bill) - bill[k]) // 2

print(billed if billed else "Bon Appetit")
