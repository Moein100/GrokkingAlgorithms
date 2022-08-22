def countlist(arr):
    if arr != [] :
        arr.pop();
        return 1 + countlist(arr);
    else:
        return 0;

def findMax(arr):
    if countlist(arr) > 1:
        maxN = arr[0];
        if maxN < findMax(arr[1:]):
            maxN=findMax(arr[1:])
        return maxN;
    else:
        return arr[0]

array= [1,2,3,4,5,6,7,8,9,10]
print(findMax(array))

