def selectSort2(arr):
    for i in range(0, len(arr)-1):
        min = arr[i]
        pos = i
        for j in range(i+1, len(arr)):
            if min > arr[j]:
                min = arr[j]
                pos = j
        arr[pos], arr[i] = arr[i], arr[pos]
        print(arr)

print("------------selectSort2--------")
arr = [9,7,25,6,8,4,3]
selectSort2(arr)