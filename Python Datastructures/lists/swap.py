def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


arr =[]
l = int(input("Enter the length of array: "))
for i in range(l):
    arr.append(int(input()))

a = arr.index(int(input("Enter Element 1: ")))
b = arr.index(int(input("Enter Element 2: ")))

swap(arr, a, b)
print(arr)