"""Python program to print even numbers in a list"""

def even_odd(arr):
    even = []
    odd = []
    for i  in arr:
        if i % 2 ==0:
            even.append(i)
        else:
            odd.append(i)
    return [even,odd]

x,y = even_odd([1,2,3,4,5,6,7,8,9,10])
print(x,y)