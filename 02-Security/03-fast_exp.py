def fast_exp(a,x):
    res = a
    arr = bin(x).replace('0b','')# First we write x in base 2

    binNum=[int(i) for e in arr for i in e]  
    l = len(binNum)
    
    # 0 = S;1 = SX
    # If the first letter is S, we raise to the square
    # otherwise, multiply by X.
    # So anyway the first thing we need to do is raise to the square
    for i in (range(l-1)):
    # We remove the first 1 of this writing,so the length is (l-1)
        res = res * res 
        # If SX then multiple by X
        if(binNum[i+1] == 1):
        # Because we remove the first 1 of this writing,we begin at binNum[i+1]
            res = res * a        
    return res

print(fast_exp(2,15))

