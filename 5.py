import math as m
print("Values of 'a' Not Allowed(because they are not reletively prime with 26:",end='')
for i in range(0,26):
    if(m.gcd(i,26)!=1):
        print(i,end=' ')
