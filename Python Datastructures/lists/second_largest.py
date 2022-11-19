"""Python program to find second largest number in a list"""


def second_largest(arr):
    max = arr[0]
    s_max = arr[0]

    for i in range(len(arr)):
        if arr[i] >= max:
            s_max = max
            max = arr[i]
            
    return s_max


print(second_largest([10, 20, 4, 45, 99]))