alpha=[ chr(a) for a in range(65,91)]
km=[['M','F','H','IJ','K'],['U','N','O','P','Q'],['Z','V','W','X','Y'],['E','L','A','R','G'],['D','S','T','B','C']]
print("PlayFlair Key Matrix\n")
for i in km:
    for j in i:
        print(j,end=' ')
    print("\n")
def encrypt(a):
    while(len(a)%2!=0):
        a+='X'
    cipher=''
    for i in range(0,len(a),2):
        for j in range(0,5):
            for k in range(0,5):
                if(km[j][k][0]==a[i][0]):
                    w=j
                    x=k
                if(km[j][k][0]==a[i+1]):
                    y=j
                    z=k
        if(w==y):
            cipher+=km[w][(x+1)%5]+km[y][(z+1)%5]
        elif(x==z):
            cipher+=km[(w+1)%5][x]+km[(y+1)%5][z]
        else:
            cipher+=km[w][z]+km[y][x]
    return cipher
print("Encrypted CIPHER:"+encrypt("SATHWIK"))
