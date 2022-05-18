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

#Merge Sort
#[4 7 1 3 14 8]
#[4 7 1] [3 14 8]
#[1 4 7] [3 8 14]
#[1 3 4 7 8 14]
def mergeSort(array):
    #base case
    if len(array) <=1:
        return array
    
    #len = 5 midIndx = 2
    midIndex = int(len(array) / 2)
    firstHalf = array[:midIndex]
    secondHalf = array[midIndex:]
    
    firstHalfSorted = mergeSort(firstHalf) #[1, 4]
    secondHalfSorted = mergeSort(secondHalf) #[2, 3, 100]
    
    arraySorted = []
    index1 = 0
    index2 = 0
    
    while index1 < len(firstHalfSorted) and index2 < len(secondHalfSorted):
        if firstHalfSorted[index1] < secondHalfSorted[index2]:
            arraySorted.append(firstHalfSorted[index1])
            index1 += 1
        else:
            arraySorted.append(secondHalfSorted[index2])
            index2 += 1            
    
    #either index1 reaches end or index2 reaches end
    if index1 == len(firstHalfSorted):
        arraySorted.extend(secondHalfSorted[index2:])
    else:
        arraySorted.extend(firstHalfSorted[index1:])
    
    return arraySorted

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

array = [55, 4, 1, 5, 3, 200, 100, 2]
#sortedArray = bubbleSort(array)
sortedArray = mergeSort(array)
print(sortedArray)
