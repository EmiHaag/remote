
def nextBitCounter(x):
    bitCounter = -1
    #count the amount of digits ex 1001011(dec75) => len(7)
    while x > 1:
        x /= 2
        bitCounter +=1

    #return the dec of that amount of digits ex 2(base) ** 7(bitcounter) == 128 (the next base 2 to follow down)
    print("next base 2 is : ", 2**(bitCounter))
    return 2**bitCounter

def counterGame(n):
    if n == 1: return 'Richard' 
    #luise starts
    # if n is power of 2 divide it by 2
    # else, find the next power to down, and passes the rest to the oponent
    # the participant that get n = 1 wins
    #returns string "Richard" or "Louise"

    #  even = luise, odds Richard 

    turno = 0    

    while(n > 1):
        turno += 1
        #if n = is power of 2
        if n and not( n & (n-1)):
            n = n // 2 
        else:
            n = n - nextBitCounter(n)
       
            

    if turno % 2 == 0: return 'Richard'
    else: return 'Louise'


print(counterGame(132))

    


