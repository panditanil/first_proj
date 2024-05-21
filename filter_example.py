#Filter example

def is_even(num):
    return num%2==0

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
list2 = filter(is_even,list1)
print(list(list2))