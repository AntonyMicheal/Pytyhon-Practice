number  = int(input("Enter the numbers: "))

a = 0
b = 1


for i in range(number):
    c = a+b
    print(a)
    a = b
    b = c

