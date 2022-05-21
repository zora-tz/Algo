#binary search
#sorted array [1 3 5 7 11 15 17]
#search for 4
#left = 0, right = 6
#mid = 3, array[3] = 7 > 4
#left = 0, right = mid = 3

#return index if found
#return -1 if not found
def binarySearch(array, element):
    left = 0
    right = len(array)-1
    mid = int(len(array)/2)

    while right != left: #[1, 5] element = 4 left = 0, right = 1, mid = 0 
        if array[mid] == element:
            return mid
        if array[mid] > element:
            right = mid - 1    
        else:
            left = mid + 1
        mid = left + int((right-left)/2)
            
    if array[right] == element:
        return right
    if array[left] == element:
        return left
    return -1

array = [1, 3, 5, 7, 11, 15, 17]
element = 2
index = binarySearch(array, element)
print(index)
