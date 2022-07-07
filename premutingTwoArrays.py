def twoArrays(k, a, b):
    # Write your code here

    # ordena dos arrays de menor a mayor
    # suma elementos espejados
    # si no es mayor a k retorna NO

    a.sort()
    b.sort()

    indA = 0
    indB = len(b)-1

    while indB >= 0:
    
        if ((a[indA] + b[indB]) < k):
            return "NO"
        indA += 1
        indB -= 1

    return "YES"


print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))
