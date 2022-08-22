def sum(arr):
    if len(arr) == 1:
        return arr[0];
    elif len(arr) == 0:
        return 0;
    else:
        return arr.pop(0) + sum(arr);
array = [2,4,6]
print(sum(array))        