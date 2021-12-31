x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

exist = False
while(True):
    if x1 == x2:
        exist = True
        break
    if (v1 > v2 and x1 > x2) or (v2 > v1 and x2 > x1) or (v2 == v1 and x2 != x1):
        break
    x1 += v1
    x2 += v2
    
if exist:
    print('YES')
else:
    print('NO')
