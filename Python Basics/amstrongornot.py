number = int(input("Enter the number: "))

n = number
amstrong_or_not = 0
while n > 0:
    rem = n % 10
    amstrong_or_not+= (rem ** 3)
    n = n//10
if amstrong_or_not == number:
    print("Amstrong")
else:
    print("Not amstrong")