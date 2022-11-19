""" Remove Multiple elements from lists"""

def elements(arr):
    for i in arr:
        if i%2==0:
            arr.remove(i)
            # or arr.pop(arr.index(i))
    
x = [1,2,3,4,5,6,7,8,9]
elements(x)
print(x)