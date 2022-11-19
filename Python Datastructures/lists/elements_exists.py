ls = [1,2,3,4,5,6,7,8,9,0]

if 4 in ls:
    print("It exists")

f = 0
for i in range(len(ls)):
    if i == 4:
        f = 1
if f == 1:
    print("I t exists")