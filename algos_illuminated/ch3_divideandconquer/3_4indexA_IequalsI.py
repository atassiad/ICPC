def binarysearchfori(arr):
    left = 0 
    right= len(arr)
    
    while (left < right): 
        middle = left + (right-left) // 2 
        if (middle < arr[middle]):
            if (left == middle):
                break
            left = middle
        elif (middle > arr[middle]):
            if (right == middle):
                break
            right = middle
        else:
            return arr[middle]
    
    return False

array1 = [0, 0, 1, 2, 3, 4, 8, 9, 10] #9 mid=5 
array2 = [1, 2, 3, 4, 5]

print(binarysearchfori(array1))
print(binarysearchfori(array2))