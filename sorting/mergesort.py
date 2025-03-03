def mergeSort(array):
    if (len(array) <= 1):
        return array
    
    arrA = mergeSort(array[:len(array)//2])
    arrB = mergeSort(array[len(array)//2:])

    return merge(arrA, arrB)

def merge(arrA, arrB):
    totalIterations = len(arrA) + len(arrB)
    arrA.append(float('inf'))
    arrB.append(float('inf'))
    returnList = []
    i = 0
    j = 0
    for k in range(totalIterations):
        if (arrA[i] < arrB[j]):
            returnList.append(arrA[i])
            i += 1
        else:
            returnList.append(arrB[j])
            j += 1
    
    return returnList

bigArr = [-20, -10, 100, -100, 50, 60, 3, 2, 1, 5]

print(mergeSort(bigArr))