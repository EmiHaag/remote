# n towers
# m = height of each tower

""" 
n number of  towers
m initial height of the tower
x current height of the tower
y new height of the tower

el jugador debe derribar partes de la torre sin dejarla en 0 

how to play: reduce size of the tower such that the new height Y is divisible by current height x
 """


def towerBreakers(n, m):
    if(m==1 or n %2 == 0):
        return 2
    else: return 1