n = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

for i in range(b, c):
    f = 0
    for j in range(2, i):
        if i%j == 0:
            f = 1
            break
    if f == 0:
        print(i, end=" ")
    