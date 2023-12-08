# given an integer array sorted
# remove duplicates in place such that each element appear only once
# the relative order of the elements should be kept the same
# return the array withpout duplicates

# example: [1,1,2] -> [1,2]
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0   
    repeated = []
    for j in range(1, len(nums)):
        if nums[i] == nums[j]:
            i += 1
            repeated.append(nums.pop(nums[j]))
    
    for i in range(len(nums)):
        if nums[i] in repeated:
            nums.remove(nums[i])
            
    return nums

listNums = []
listNums = input().split(",")
print(removeDuplicates(listNums))