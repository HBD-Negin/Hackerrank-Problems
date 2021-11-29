def factors(n):
	temp = []
	for i in range(1, n+1):
		if n%i == 0:
			temp.append(i)
	return temp

def commonmat(matrx):
	temp = matrx[0]
	for i in matrx:
		temp = list(set(temp).intersection(i))
	return temp

counts = raw_input()
a = list(map(int, raw_input().split(" ")))
b = list(map(int, raw_input().split(" ")))

fList = []

for i in b:
	tList = factors(i)
	fList.append(tList)

fList = commonmat(fList)
sList = []

for i in fList:
	flag = 1
	for j in a:
		if i%j != 0:
			flag = 0
			break
	if flag == 1:
		sList.append(i)

print len(sList)