n = input()
st = raw_input()
li = st.split()
max = int(li[0])
for i in range(n):
    tmp = int(li[i])
    if tmp > max :
        max = tmp
count = 0
for i in range(n):
    tmp = int(li[i])
    if tmp == max :
        count += 1
print(count)