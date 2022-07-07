def sockMerchant(n,ar):
    pairs = 0
    #get the maximum value from the list
    maxVal = max(ar)

    #create list with 0 for counting each
    counter=[]
    for e in range(maxVal + 1):
        counter.append(0)

    #get the current val from ar and sum it to counter with his respective position
    for ind in ar:
        counter[ind] += 1

    #sum the pairs for each
    for c in counter:
        pairs += c // 2

    #return total of pairs 
    return pairs

sockMerchant(7,[1,2,1,2,1,3,2])