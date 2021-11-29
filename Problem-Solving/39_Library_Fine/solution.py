dr, mr, yr = map(int, input().split())
de, me, ye = map(int, input().split())
fine = 0
if dr <= de and mr <= me and yr <= ye:
    fine = 0
elif dr > de and mr == me and yr == ye:
    fine = 15*(dr-de)
elif mr > me and yr == ye:
    fine = 500*(mr-me)
elif yr > ye:
    fine = 10000
print(fine)