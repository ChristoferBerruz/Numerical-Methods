def mysqrt1(n: int, e: float) -> int:
    """"
    First guess is g = n/2
    Each iterative guess is in the form g_new = (g_old + n/g_old)/2.
    Stops once tolerance is achieved.
    """
    g = n/2
    while(abs(g**2-n)>e):
        g = (g + n/g)/2
    return g


def mysqrt2(n: int, e: float) -> int:
    """
    This method uses a trial and error algorithm.
    #Finds the biggest positive integer g so that n - g**2 > 0.
    #Finds the biggest digit d placed at a decimal place p so that n - g.d**2 > 0
    #Stops once tolerance is achieved.
    """
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


#Please change this parameters as test values
n = 11
e = 0.0001
#Testing each function
g1 = mysqrt1(n,e)
g2 = mysqrt2(n,e)
#Printing to console
print(g1)
print(g2)
