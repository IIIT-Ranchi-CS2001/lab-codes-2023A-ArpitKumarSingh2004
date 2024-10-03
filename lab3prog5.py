s=input("ENTER THE STRING : ")
b=False
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
         b=True
    elif s[i]>='a' and s[i]<='z':
         b=True
    elif s[i]>='0' and s[i]<='9':
         b=True
    else:
         b=False
         break
print(b)
