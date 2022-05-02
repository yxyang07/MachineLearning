# To calculate the time required for this algorithm
import time
start =time.perf_counter()

#--------------------------------------------------
# c is a prime;m is not a multiple of c,so they are coprime integers
# Each prime number p dividing m, (a−1) is a multiple of p.
# m and (a-1) are multiple of 4
a = 1664525
c = 1013904223
m = 2**32
RandNum = 1

def LCG(a,c,m):
    global RandNum
    # Xn+1=(a⋅Xn+c)%m
    RandNum = (a*RandNum + c) % m
    return RandNum

# Generate 10 random numbers
for i in range(10):
    print(LCG(a, c, m))
# the frequency of occurrence of even and odd numbers is 50%

#--------------------------------------------------
# To calculate the time required for this algorithm
end = time.perf_counter()
print('Running time: %s Seconds'%(end-start))
