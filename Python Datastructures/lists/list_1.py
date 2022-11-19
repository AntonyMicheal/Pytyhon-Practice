def elements_of_list(n,ls):
    x = int(input("Enter: "))
    ls.append(x)
    if n >0:
        elements_of_list(n-1, ls)
    else:
        print(ls)

ls = []
elements_of_list(5,ls)