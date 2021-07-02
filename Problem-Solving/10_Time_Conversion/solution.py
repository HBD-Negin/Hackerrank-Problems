st = raw_input()
if st[-2] == 'A' :
    li = st.split(':')
    if li[0] == '12' :
        li[0] = '00'
    st = ':'.join(li)
    st = st[:-2]
else :
    li = st.split(':')
    tmp = int(li[0])
    if tmp != 12 :
        tmp += 12
    li[0] = str(tmp)
    st = ':'.join(li)
    st = st[:-2]
print(st)