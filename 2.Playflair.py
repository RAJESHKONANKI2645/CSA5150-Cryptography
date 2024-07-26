km=[['0','0','0','0','0'] for i in range(5)]
alpha=[chr(i) for i in range(65,91)]
def cipher(a,b):
    if(a=='J'):
        a='I'
    elif(b=='J'):
        b='I'
    for i in range(5):
        for j in range(5):
            if(a==km[i][j][0]):
                w=i
                x=j
            if(b==km[i][j][0]):
                y=i
                z=j
    if(w==y):
        return km[w][(x+1)%4],km[y][(z+1)%4]
    elif(x==z):
        return km[(w+1)%5][x],km[(y+1)%5][z]
    else:
        return km[w][z],km[y][x]
p=input("Enter the Plain Text:").upper()
k=list(input("Enter the Key:").upper())
for i in k:
    if(k.count(i)>1):
        k.remove(i)
k=''.join(k)
y,z,f=0,0,0
for i in k:
    if(z==5):
        z=0
        y+=1
    if(i=='I' or i=='J'):
        if(f==0):
            km[y][z]='IJ'
            f=1
            z+=1
            continue
        else:
            continue
    km[y][z]=i
    z+=1
for i in alpha:
    if(z==5):
        z=0
        y+=1
    if i not in k:
        if(i=='I' or i=='J'):
            if(f==0):
                print(i)
                km[y][z]='IJ'
                f=1
                z+=1
                continue
            else:
                continue
        km[y][z]=i
        z+=1
for i in range(5):
    for j in range(5):
        print(km[i][j],end=' ')
    print("\n")
if(len(p)%2==1):
    p+='X'
c=['0' for i in range(len(p))]
for i in range(0,len(p),2):
    c[i],c[i+1]=cipher(p[i],p[i+1])
c=''.join(c)
print("Encryption\nCipher Text:",c)
print("Decryption\nPlainText:",p)
