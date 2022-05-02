import random
from math import pow


a=random.randint(2,10) #We randomly choose a value a from 2 to 10

#To get the gcd of a and b, gcd(a, b) = 1.
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)

#Randomly select a large prime P, and P-1 is required to have a large prime factor. Then choose an primitive of module P α。 Add P and α Open.
#Randomly select an integer D as the key, 2 ≤ D ≤ P-2.
#Calculate y= α^ D mod p, take y as the public key.
def Generate_Key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key

#To obtain the prime factors of n
def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c
        y=(y*y)%c
        b=int(b/2)
    return x%c

# For plaintext m encryption, randomly select an integer k, 2 ≤ K ≤ P-2
# C1＝ α^ k mod p
# C2＝MY^k mod p
# Ciphertext is (C1, C2)
def encryption(msg,q,h,g):
    ct=[]
    k=Generate_Key(q)
    s=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,p

# Plaintext M can be obtained from ciphertext, M = C2 / C1 ^ D mod P
def decryption(ct,p,key,q):
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt


msg=input("Please input your message >>>>>")
q=random.randint(pow(10,20),pow(10,50))
g=random.randint(2,q)
key=Generate_Key(q)
h=power(g,key,q)
print("g =",g,"g^a =",h)
ct,p=encryption(msg,q,h,g)
print("Our Original Message is = ",msg)
print("The Encrypted Message is = ",ct)
pt=decryption(ct,p,key,q)
d_msg=''.join(pt)
print("The Decrypted Message is = ",d_msg)