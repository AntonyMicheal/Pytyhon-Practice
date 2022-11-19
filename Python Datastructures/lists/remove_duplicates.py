"""
Python | Program to print duplicates from a list of integers
"""

"""
def duplicates(arr):
    s = []
    for i in arr:
        if arr.count(i) > 1 and i not in s:
            s.append(i)
    return s
"""
"""def duplicates(arr):
    s = set()
    for i in range(len(arr)):
        if arr[i] in arr[i+1:len(arr)]:
            s.add(arr[i])
    return s"""


def duplicates(arr):
    pass


x = duplicates([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20])
print(x)