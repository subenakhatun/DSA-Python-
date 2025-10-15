li = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
target_value = 80
start = 0
end = len(li)-1
# print(len(li))
# print(end) 
def binary_search(li,target_value):
    while(start <= end):

        mid = start+end//2
        if mid == target_value:
            return mid
        elif mid < target_value:
            start = mid +1
            




# result = binary_search(li,target_value)