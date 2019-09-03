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
    if n == 0: return 0
    bound = int(n/2) + 1
    result = ''
    g = 0
    for i in range(bound):
        if (n-i**2)*(n-(i+1)**2)<0:
            g = i
            break
        elif (n-i**2)*(n-(i+1)**2)==0:
            g = i+1
            break
    tenth = 0.10
    while(abs(n-g**2)>e):
        for j in range(1,10):
            r1 = g + tenth*j
            r2 = g + tenth*(j+1)
            if (n-r1**2)*(n-r2**2)<0:
                g = g + tenth*j
                break
        tenth = tenth*0.10
    return g


#Please change this parameters as test values
n = 1
e = 0.00001
#Testing each function
g1 = mysqrt1(n,e)
print(g1)
g2 = mysqrt2(n,e)
print(g2)
