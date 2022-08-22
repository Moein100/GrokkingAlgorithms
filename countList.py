def countlist(arr):
    if arr != [] :
        arr.pop();
        return 1 + countlist(arr);
    else:
        return 0;
array = [1, 2, 3, 4, 5, 6, 7, 8];
print(countlist(array))