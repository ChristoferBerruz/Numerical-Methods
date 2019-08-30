import math
def mysqrt1(n, e):
    g = n/2
    while(abs(g**2-n)>e):
        g = (g + n/g)/2
    print(g)

def mysqrt2(n,e):
    #Initial guess
    bound = int(n/2)
    result = ''
    g = 0
    for i in range(bound):
        if (n-i**2)*(n-(i+1)**2)<0 or (n-i**2)*(n-(i+1)**2)==0:
            g = i
    result = str(g) + '.'
    while(abs(n-g**2)>e):
        for i in range(10):
            r1 = result + str(i)
            r2 = result + str(i+1)
            if (n-float(r1)**2)*(n-float(r2)**2)<0:
                result = result + str(i)
        g = float(result)
    print(result)


mysqrt1(11,0.00001)
mysqrt2(11, 0.0001)
