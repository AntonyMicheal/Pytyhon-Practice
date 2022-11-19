"""Find sum and average of List in Python"""

def sum_avg(arr):
    sum = 0
    for i in arr:
        sum+=i
    return f"sum = {sum} \naverage = {sum/len(arr)}"

print(sum_avg([1,2,3,4,5,6,7,8,9,10]))