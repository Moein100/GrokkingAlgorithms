def countList(arr):
    if arr != [] :
        return 1 + countList(arr[1:]);
    else:
        return 0;

def findMax(arr):
    if countList(arr) != 1:
        maxN = arr.pop();
        nextN = findMax(arr);
        if maxN < nextN:
            maxN=nextN
        return maxN
    else:
        return arr[0]

array= [1,2,3,4,5,6,7,8,9,10]
print(findMax(array))

