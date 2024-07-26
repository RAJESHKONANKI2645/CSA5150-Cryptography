alpha=[chr(i) for i in range(65,91)]
print(alpha)
p=input("Enter the Plain Text:")
k=int(input("Enter the Key:"))
c=''
for i in p:
    c+=alpha[(alpha.index(i.upper())+k)%26]
print("Cipher Text:",c,sep=' ')
