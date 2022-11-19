ls = [1,70,5,80,3,4,2]

max = ls[0]
sec_max = ls[0]
for i in range(len(ls)):
    if sec_max < ls[i]:
        sec_max = ls[i]
    if sec_max > max:
        temp = max
        max = sec_max
        sec_max = temp
print(max, sec_max)
