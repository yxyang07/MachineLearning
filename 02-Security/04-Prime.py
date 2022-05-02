def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)# Create the list of integers from 0 to N
    #I will limit the scale from 2 to N later 
    p = 2 # Because it is the smallest prime
    while p * p <= n:# until sqrt(n)
        if primes[p]:# If it's not sifted, it must be prime
            for i in range(p * 2, n + 1, p):# Just sift out its multiples
                primes[i] = False
        p += 1
    primes = [element for element in range(2, n) if primes[element]]
    # Limit the range from 2 to N and get all primes less than n
    return primes

print(sieve_of_eratosthenes(100))
# Not suitable for computer security.
# The time complexity is too high and depends on memory