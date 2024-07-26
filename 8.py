alpha=[chr(a) for a in range(65,91)]
key='CIPHER'
st=list(key)
for i in alpha:
    if i not in key:
        st.append(i)
def encryption(a):
    print("The Encrypted Text:",end='')
    s=''
    for i in a:
        s+=st[alpha.index(i)]
        print(st[alpha.index(i)],end='')
    return s
def decryption(a):
    print("\nThe Decrypted Text:",end='')
    for i in a:
        print(alpha[st.index(i)],end='')
pt=input("Enter the Plain Text:")
decryption(encryption(pt))
