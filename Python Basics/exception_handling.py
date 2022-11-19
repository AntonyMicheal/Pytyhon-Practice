try:
    age = int(input("Enter age: "))
    print(age/0)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("Xero division")
    