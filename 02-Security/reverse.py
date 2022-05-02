def egcd(a, b):
    if a == 0:
        print("yes")
        return (b, 0, 1)
    else:
        print("1a,b=",a,b)
        g, y, x = egcd(b % a, a)
        print("a,b=",a,b)
        print("the x time",g,y,x)
        print(g, x - (b // a) * y, y)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    print('result',g,x,y)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        print("x=",x,"m=",m)
        return x % m
    
print(modinv(17,300))