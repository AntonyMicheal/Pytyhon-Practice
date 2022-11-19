def interchange(arr):
    temp = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = temp
    return arr
    
arr = [1,2,3,4,5,6,7,8,9]
print(interchange(arr))