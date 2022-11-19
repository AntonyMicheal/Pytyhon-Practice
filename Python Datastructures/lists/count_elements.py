"""Count occurrences of an element in a list"""

def count_occurances(arr, n):
    if n in arr:
        return f"count of {n} in list is: {arr.count(n)}"
    else:
        return f"{n} not present in the list"


def count_occurance(arr, n):
    count = 0
    if n in arr:
        for i in arr:
            if i == n:
                count += 1
        return f"count of {n} in list is: {count}"
    else:
        return f"{n} not present in the list"

arr = [1,1,2,2,2,6,6,7,1,6,8,8,8,6,10,1,4,5,6,7,9,0,3,4]
print(arr)
print(count_occurances(arr, 4))
print(count_occurance(arr, 8))