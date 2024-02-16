# //  https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

def removeElement(arr, value) -> int:
    for i in range(0, len(arr)-1):
        if arr[i] == value:
            arr.remove(arr[i])
    return len(arr)


arr = []
value = 0

arr = []
fim = True
while fim:
    elementArray = input()
    if elementArray  != "[" and elementArray != "]" and elementArray != "," and elementArray != "":
        arr.append(elementArray)
        print(arr)
    elif len(elementArray) > 0 and elementArray[-1] == "]":
        value = input()
        fim = False

print(removeElement(arr, value))