#binary search
#for a sorted array with duplicated element
#find first and last appearance

def binarySearch(array, element):
    left = 0
    right = len(array)-1
    while left != right:
        midIndex = int((right - left)/2) + left
        if array[midIndex] > element:
            right = midIndex - 1
        if array[midIndex] < element: 
            left = midIndex + 1
        
        if array[midIndex] == element:
            first = midIndex
            last = midIndex
            while first-1 >= 0 and array[first-1] == element:
                first -= 1
            while last+1 < len(array) and array[last+1] == element:
                last += 1
            print(first)
            print(last)
            return first, last
        
def binarySearchV2(array, element):
    left = 0
    right = len(array)-1
    while left != right:
        midIndex = int((right - left)/2) + left
        if array[midIndex] > element:
            right = midIndex - 1
        if array[midIndex] < element: 
            left = midIndex + 1
        
        if array[midIndex] == element:
            right = midIndex
    
    if array[left] == element:
        return left
    else:
        return -1
    
array = [0, 1, 1, 3, 6, 11]
index = binarySearchV2(array, 2)
print(index)