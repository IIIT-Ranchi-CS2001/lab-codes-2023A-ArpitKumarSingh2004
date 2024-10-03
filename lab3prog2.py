a=int(input("ENTER THE VALUE OF n: "))
print("ENTERED NUMBER IS: ",a)
sum=0
while(a>0):
     d=a%10
     sum=sum+d
     a=a//10
print("SUM OF DIGIT : ",sum)
