# If n is prime and a and n are coprime,
# then the remainder of the (n-1) power of a divided by n is equal to 1
def Small_Fermat(x, n, p):
  # If n is an even number, then x ^ n = (x * x) ^ [n / 2];
  # If n is an odd number, then x ^ n = x * x ^ (n-1) = x * (x * x) ^ [n / 2];
  if n == 0:
    return 1
  # 2 * * (n-1)% n is not an easy number to calculate. 
  # We use modular operation to calculate x ^ n (% P)
  res = Small_Fermat((x*x)%p, n>>1, p)
  if n&1 != 0:
    res = (res*x)%p
  return res

def fermat_test_prime(n):
  if n == 1:# If the input number =1 then it's not prime
    return False
  if n == 2:# If the input number =2 then it's prime 
    return True
  res = Small_Fermat(2, n-1, n)# We choose 2 as the number a
  return res == 1

print(fermat_test_prime(1))