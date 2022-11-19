a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

for i in range(a,b):
    n = i
    amstrong_or_not = 0
    while n > 0:
        rem = n%10
        amstrong_or_not += (rem **3)
        n = n//10

    if amstrong_or_not == i:
        print(i, end=" ")
