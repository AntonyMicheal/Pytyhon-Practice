# Opening and reading a file.

"""file = open("Python Special Programs/test.txt", "r")
x = file.read()
print(x)
"""
# Writing into a file
"""file_2 = open("Python Special Programs/test_2.txt", "w")
file_2.write("Pinki \nRed")
file.close()
"""

x = ["red", "Blue", "Orange", "Pink", "King"]

file_2 = open("Python Special Programs/test_3.txt", "w")

for item in x:
    file_2.write(item +"\n")


file_2.close()

file_3 = open("Python Special Programs/test_3.txt", "r")
x = file_3.read()
print(x)