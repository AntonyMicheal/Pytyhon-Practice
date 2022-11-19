"""Program to enter elements into the list and displaying them."""

def input_elements(n, arr):
    for i in range(n):
        arr.append(int(input()))

def printry(arr):
    print(" ".join(arr))

l = int(input("Enter the length of the list: "))
arr = []
input_elements(l, arr)
printry(arr)