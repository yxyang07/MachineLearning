# Integrate this random generator tool to one-time pad
a = 1664525
c = 1013904223
m = 2**32
Rand = 1
pad ={}

#generate random bits 
def RandomNum(a,c,m):
    global Rand
    Rand = (a*Rand + c) % m
    return Rand 

def XOR(msg,pad,length):
    return ([msg[i] ^ pad[i] for i in range(length)])

#0 0 1 0 0 1 0 1 0 0 0 1 1 1 1 0 0 1 1 1 1 1 1 1 0
arr = input("")    
msg = [int(n) for n in arr.split()]    
l = len(msg)

for i in range (l):
    pad[i]=RandomNum(a, c, m)

cipher = XOR(msg,pad,l)
print("The pad is:",pad)
print("The cryptogram is:",cipher)
print("The original message is:",XOR(cipher,pad,l))
