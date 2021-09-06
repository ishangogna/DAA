#insertion sort

def insertionSort(arr):
    lenArr = len(arr)
    for i in range(1,lenArr):
        current = arr[i]
        j = i-1
        while(j >=0 and arr[j]> current):
            arr[j+1] = arr[j]
            j = j-1
        
        arr[j+1] = current
    print(arr)

insertionSort([8,2,1,4,5])



