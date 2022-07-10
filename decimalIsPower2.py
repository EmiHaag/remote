def esPotencia2(n):
    if n and not( n & (n-1)):
        print("n : ", n, " es potencia de 2")
        return True
    else:
        print("n :", n, " no es potencia de 2")
        return False


