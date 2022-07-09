def balancedSum(arr):
    #returns yes or not if the sum of left and right subarrays from current ind is equal
    # ex arr [1,2,3,3]
    # arr[0] + arr[1] = arr[3]
    # we have to ask the arr[0]+arr[1]+arr[2]+arr[3] - arr[idx] / 2 = sum ? YES OR NO
    currentSum = 0
    arrSum =sum(arr)

    for idx, i in enumerate(arr):
       
        print("if ",arrSum , " - " , arr[idx] ,  " / 2" " == ", currentSum)
        if (arrSum - arr[idx]) // 2 == currentSum: 
            return "YES"
        else:
            currentSum += i
    return "NO"

print(balancedSum([1,2,3,3]))


