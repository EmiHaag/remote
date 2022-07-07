def findMedian(arr):
    # Write your code here
    
    arr.sort()
    indMed = len(arr) //2
    return arr[indMed]




print(findMedian([0,1,2,4,6,5,3]))