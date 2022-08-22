def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index;
def manualSort(arr):
    result = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        result.append(arr.pop(smallest))
    return result

array = [23,1,4,12,34,12,1]
print(manualSort(array));