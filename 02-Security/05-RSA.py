import random 

#Use extended Euclidean algorithm to find the mod reverse
#--------------------------------------------------------
#Based on Euclidean theorem: GCD (a, b) = GCD (B, a% B),
#we can easily find the maximum common factor of a and B

#For nonnegative integers a, B, GCD (a, b) that are not completely 0,
#GCD (a, b) represents the maximum common divisor of a and B. 
#There must be an integer pair x, y, so that GCD (a, b) = a * x + b * y.
def pgcd(a,b):
    if a == 0:
        #When one of a or b is zero, let a number be the desired GCD. 
        #Therefore, the stop state of Euclidean algorithm is: b = GCD, a = 0
        return (b,0,1)
    else:
        x,y,q = pgcd(b%a, a)# Apply the Euclidean theorem
        return (x, q - (b//a) * y, y)
       
    
def Mod_Reverse(a,m):
    x,y,q= pgcd(a,m)
    if x!=1:# If it is not coprime, there is no solution
        return "There is no Mod_Reverse"
    else:
        return y%m

#--------------------------------------------------------

#Use the small fermat theory to get the list of Prime
def Small_Fermat(x, n, p):
  if n == 0:
    return 1
  res = Small_Fermat((x*x)%p, n>>1, p)
  if n&1 != 0:
    res = (res*x)%p
  return res

def IsPrime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  res = Small_Fermat(2, n-1, n)
  return res == 1


def Get_Prime(x,y):
    prime_list=[]
    for i in range(x,y):# Create a list of integer from x to y
        if IsPrime(i):# For every integer judge if it is prime
            prime_list.append(i)# If it is prime we append it in the prime list
    return prime_list

#--------------------------------------------------------
# The same set of methods can be used for encryption and decryption:
# The so-called "encryption" is to calculate ans of the following formula: msg ^ c ≡ ans (MOD n)
# Decryption requires a private key
def d_encrypt(a,b,c):
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a % c) * (a % c)
    return ans
    
#--------------------------------------------------------
         
def RSA_key():
    RSA_KEY = {}
    # Randomly select two unequal prime numbers P1 and P2
    prime_arr = Get_Prime(10,100)#Get a list of Primes from 10 to 100
    #Randomly choose from the list
    P1 = random.choice(prime_arr)
    P2 = random.choice(prime_arr)
    #If we get the equal P1 and P2 we will select until they are unequal
    while P1 == P2:
        P2 = random.choice(prime_arr)
    #The length of n written in binary is the key length. 
    n = P1 * P2
    #Calculating the Euler function (s) of n 
    s = (P1-1)*(P2-1)
    #Randomly choose a number c,c and s are coprime.
    c = 65537
    # Calculate c for s Modular inverse element d
    d = Mod_Reverse(c,s)
    print("P1=",P1,"P2=",P2,"n=",n,"s=",s,"c=",c,"d=",d)
    public_key = [n,c]
    private_key = [n,d]
    RSA_KEY['pub']=public_key
    RSA_KEY['priv']=private_key
    return RSA_KEY
      
msg = int(input("Please input your message >>>>>"))
# The message cannot be bigger than n
RSA_k = RSA_key() 
pub_k = RSA_k['pub']
priv_k = RSA_k['priv']
#Use the public key to encrypt the message 
encrypt = d_encrypt(msg, pub_k[1], pub_k[0])
print("The encrypt messsage is:",encrypt)
decrypt = d_encrypt(encrypt, priv_k[1], priv_k[0])
print("The decrypt message is:",decrypt)

    
    
    