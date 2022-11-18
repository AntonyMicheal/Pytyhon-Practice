x = [1,2,3,4,5]
y = [5,2,4,1,7]
print(x)
print(x.index(3))
print(x[::-1])
print(x[::-2]) # -> skips an element.

# sort alters the entire list so copy the list to another variable and use that copy for safety
y.sort()
print(y)
