def mysqrt1(n, e):
    g = n/2
    while(abs(g**2-n)>e):
        g = (g + n/g)/2
    return g

def mysqrt2(n,e):
    #Initial guess
    bound = int(n/2)
    result = ''
    g = 0
    for i in range(bound):
        if (n-i**2)*(n-(i+1)**2)<0 or (n-i**2)*(n-(i+1)**2)==0:
            g = i
            break
    result = str(g) + '.'
    while(abs(n-g**2)>e):
        for j in range(10):
            r1 = result + str(j)
            r2 = result + str(j+1)
            if (n-float(r1)**2)*(n-float(r2)**2)<0:
                result = result + str(j)
                break
        g = float(result)
    return g

mysqrt1(17,0.00001)
mysqrt2(17, 0.00001)
