def maxrecuni(arr): #O(N)
    arrLen = len(arr)
    if (arrLen == 1):
        return arr[0]
    leftVal = maxrecuni(arr[0:arrLen // 2])
    rightVal = maxrecuni(arr[arrLen//2:arrLen])

    return max(leftVal, rightVal)

def binarysearchuni(arr):
    left = 0 
    right= len(arr)
    
    while (left < right): 
        middle = left + (right-left) // 2 
        prev = max(0, middle-1) #4
        next = min(right-1,middle+1) #6
        if (arr[next] > arr[middle]):
            left = middle
        elif (arr[prev] > arr[middle]):
            right = middle
        else:
            return arr[middle]
    
    return False


#find the max element in these unimodal arrays in log(n) time 
array1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
array2 = [-10, 0, 10 ,20, 40, 100, 1000, 900, 800, 750, 500, 11, 9, 7, 5]
array3 = [1,5,2]
array4 = [1, 5]
array5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0] 
array6 = [1, 2, 3, 4, 5]

#return results O(n)
#print(maxrecuni(array1))
#print(maxrecuni(array2))
#print(maxrecuni(array3))
#print(maxrecuni(array4))

#return results O(log(n))
print(binarysearchuni(array1))
print(binarysearchuni(array2))
print(binarysearchuni(array3))
print(binarysearchuni(array4))
print(binarysearchuni(array5))
print(binarysearchuni(array6))