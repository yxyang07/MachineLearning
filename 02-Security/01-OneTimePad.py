import numpy as np

# Random bits generator(the key/noise)
# Only Generate 0 and 1,same length as the original message
def RandomNum(n):
    return np.random.randint(0,2,size=n) 

# Performe the bit by bit exclusive OR 
# The 2 message must have the same length
def XOR(msg,pad,length):
    return ([msg[i] ^ pad[i] for i in range(length)])


# 0 0 1 0 0 1 0 1 0 0 0 1 1 1 1 0 0 1 1 1 1 1 1 1 0
arr = input("")# Define the original message
msg = [int(n) for n in arr.split()]    
l = len(msg)

mask = RandomNum(l)
cipher = XOR(msg,mask,l)

# We use the same key to mask and unmask the origianl message
print("The mask is:",mask)
print("The cryptogram is:",cipher)
print("The original message is:",XOR(cipher,mask,l))
