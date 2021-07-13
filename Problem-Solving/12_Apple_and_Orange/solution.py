fst = raw_input().split()
snd = raw_input().split()
thd = raw_input().split()
frt = raw_input().split()
fft = raw_input().split()
s = int(fst[0])
t = int(fst[1])
a = int(snd[0])
b = int(snd[1])
m = int(thd[0])
n = int(thd[1])
apl = 0
orn = 0
for i in range(m):
    tmp = a + int(frt[i])
    if (tmp >= s and tmp <= t):
        apl += 1
for i in range(n):
    tmp = b + int(fft[i])
    if (tmp >= s and tmp <= t):
        orn += 1  
print apl
print orn