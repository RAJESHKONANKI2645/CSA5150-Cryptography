import math
import random
alpha=[chr(i) for i in range(65,91)]
p=input("Enter the Plain Text:").upper()
k=input("Enter the Key:").upper()
n=math.ceil(math.sqrt(len(k)))
km=[['0' for i in range(n)] for j in range(n)]
r=0
for i in range(len(k),n*n):
    while(1):
        if alpha[r] not in k:
            k+=alpha[r]
            break
        r+=1
r=0
for i in range(n):
    for j in range(n):
        km[i][j]=alpha.index(k[r])
        r+=1
while(len(p)%n!=0):
    p+='X'
pm=[['0' for i in range(1)] for i in range(n)]
print("Key Matrix:")
for i in range(n):
    for j in range(n):
        print(km[i][j],end=' ')
    print("\n")
def encrypt(r):
    for i in range(n):
        for j in range(1):
            pm[i][j]=alpha.index(p[r])
            r+=1
    l=[0 for i in range(n)]
    for i in range(n):
        for j in range(1):
            for k in range(n):
                l[i]+=km[i][k]*pm[k][j]
        print(alpha[l[i]%26],end='')
print("Encryption:\nCipher Text:",end='')
for i in range(0,len(p),n):
    encrypt(i)
print("\nDecryption:\nPlain Text:",p)
