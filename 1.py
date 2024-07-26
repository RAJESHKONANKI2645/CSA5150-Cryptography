alpha=[chr(i) for i in range(65,91)]
print(alpha)
p=input("enter the plain text")
k=int(input("enter the key:"))
c=''
for i in p:
    c+=alpha[(alpha.index(i.upper())+k)%26]
print("ENCRYPTION\nCipher Text:",c,sep='')
p=''
for i in c:
    p+=alpha[(alpha.index(i)-k)%26]
print("DECRYPTION\nCipher Text:",p,sep='')             
               
      
