"""Python | Sum of number digits in List"""

def sum_of_digits(arr):
    l = []
    for i in arr:
        digit = 0
        while i > 0:
            rem = i%10
            digit+=rem
            i = i//10
        l.append(digit)
        digit = 0
    return l


print(sum_of_digits([12,67,98,34]))