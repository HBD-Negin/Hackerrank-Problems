def extraLongFactorials(n):  
   if n == 1:  
       return n  
   else:  
       return n * extraLongFactorials(n-1)  

n = int(input())
print(extraLongFactorials(n))