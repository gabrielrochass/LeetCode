# //  https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

def removeElement(arr, value) -> int:
    for i in range(0, len(arr)):
        if arr[i] == value:
            arr.pop(arr[i])
    return len(arr)


arr = []
value = 0
# carac = '['
end = ']'

arr = []
element = input()

while True:
    elementArray = input().split(",")
    if elementArray == end or elementArray[-1] == end:
        break
    arr.append(elementArray) # creating array

value = input()
print(removeElement(arr, value))