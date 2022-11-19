"""Python program to find smallest number in a list"""

def smallest(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

print(smallest([-7,5,1,3,7,-9]))

