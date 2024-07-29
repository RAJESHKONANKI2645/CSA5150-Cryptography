alpha=[chr(a) for a in range(65,91)]
km=[[9,4],[5,7]]
pt="meet me at the usual place at ten rather than eightoclock"
pt=pt.replace(" ",'').upper()
def hill(a,b):
    a,b=alpha.index(a),alpha.index(b)
    l=[[a],[b]]
    r=[[0],[0]]
    for i in range(2):
        for j in range(1):
            for k in range(2):
               r[i][j]+= km[i][k]*l[k][j]
    print(alpha[r[0][0]%26]+alpha[r[1][0]%26],end='')
while(len(pt)%2!=0):
    pt+='X'
print("Cipher Text=",end='')
for i in range(0,len(pt),2):
    hill(pt[i],pt[i+1])
