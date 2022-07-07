def dynamic(n, queries):
    #params
    #int n: the number of empty arrays to initialize in 
    # string queries[q]: query strings that contain 3 space-separated integers

    #initialize 0 values in n arrays
    arr = [[] for j in range(n)]

    lastAnswer = 0
    response = []
    
    #parse strings to int arrays of queries
    for q in queries:

        typeQ = q[0]
        x = q[1]
        y = q[2]

        idx = ((x ^ lastAnswer) % n)
        
        if(typeQ == 1):        
            
            arr[idx].append(y)

        else:
            #typeq = 2
            lastAnswer = arr[idx][y % len(arr[idx])]
            response.append(lastAnswer)
    
    return response

   
    
  


    #RETURN int[]: the results of each type 2 query in the order they are presented



print(dynamic(2, [[1, 0, 5,], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]))