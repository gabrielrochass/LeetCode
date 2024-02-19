# given array in increasing order, remove duplicates in place such that each element appear only once and return the new length
#  the relative order of elements should be kept the same
#  [1, 1, 2] => 2
#  [0,0,1,1,1,2,2,3,3,4] => 5
def removeDuplicates(arr):
    if len(arr) == 0:
        return 0
    # iterate the list 2 by 2, if the second one is eqaul to first one, remove the second
    for i in range(0, len(arr)-2):
        if i+1 < len(arr) and arr[i] == arr[i+1]:
            arr.remove(arr[i+1])
    
    # return the length of the list
    return len(arr)

# arr = [1,1,2]
# result = removeDuplicates(arr)
# print(result)

arr = []
# recebe o input
while True:
    elementArray = input().split(",")
    if elementArray != "":
        arr.append(elementArray)
        # print(arr)
    else:
        break
print(removeDuplicates(arr))
