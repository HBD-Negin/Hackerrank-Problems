year = int(input().strip())

if year == 1918:
    result = '26.09.1918'
elif ((year <= 1917) & (year % 4 == 0)) or ((year % 400 == 0) or ((year % 4 == 0) & (year % 100 != 0))):
    result = '12.09.%s' %year
else:
    result = '13.09.%s' %year

print(result)
