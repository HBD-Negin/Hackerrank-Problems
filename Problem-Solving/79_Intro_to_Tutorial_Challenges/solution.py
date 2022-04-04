def introTutorial(V, arr):
    return arr.index(V)

V = int(input().strip())
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = introTutorial(V, arr)
print(str(result) + '\n')