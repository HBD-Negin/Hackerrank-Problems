n, k, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    temp = int(input())
    ind = (temp-k)%n 
    print(arr[ind])
