""" Remove empty tupples"""

def remove_tuples(arr):
    for i in arr:
        if len(i) == 0:
            arr.remove(i)

x = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
print(x)
remove_tuples(x)
print(x)