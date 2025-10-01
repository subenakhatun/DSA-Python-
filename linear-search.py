# linear Search algorithm

"""
Work Flow:
1. Define a array or list
2. Difne a targer value what you want to search or find from this list
3. Make a fucntion linearSearch()
4. apply codition for searching
5. return function
6. call function

"""
list1 = [10,20,30,40,50,60,70,80,90,20,100]
target_value = 20
def linearSearch(list1,target_value):
    for i in range(len(list1)):
        if list1[i] == target_value:
            return i
    # return -1
result = linearSearch(list1,target_value)
print(result)
