# Bubble sort
# For each iteration, the the smallest element and put it to the leftmost
# [4 3 1 2]
# [1 3 4 2]
# [1 2 4 3]
# [1 2 3 4]
def bubbleSort(array):
    for i in range(len(array)):
        currentSmallIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[currentSmallIndex]:
                currentSmallIndex = j
        swap(array, i, currentSmallIndex)        
    return array

def mergeSort(array):
    return

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

array = [4, 1, 3, 100, 2]
sortedArray = bubbleSort(array)
print(sortedArray)
