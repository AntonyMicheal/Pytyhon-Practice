def enter_elements(n, ls):
    for i in range(n):
        ls.append(int(input("Enter: ")))


def interchange(ls):
    temp = ls[0]
    ls[0] = ls[-1]
    ls[-1] = temp

def print_elements(ls):
    print(ls)


ls = []
enter_elements(5,ls)
print_elements(ls)
interchange(ls)
print_elements(ls)