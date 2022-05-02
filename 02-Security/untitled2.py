a = 1664525
c = 1013904223
m = 2**32
RandNum = 1

def LCG(a,c,m):
    global RandNum
    RandNum = (a*RandNum + c) % m
    return RandNum


for i in range(10):
    print(LCG(a, c, m))
    