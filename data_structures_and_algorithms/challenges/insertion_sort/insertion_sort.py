def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i-1
        temp=arr[i]
        while j>=0 and temp<arr[j]:
            arr[j+1]= arr[j]
            j = j-1
        arr[j + 1] = temp
    return arr


insertion_sort([20,18,12,8,5,-2])      
insertion_sort([5,12,7,5,5,7])      
insertion_sort([2,3,5,7,13,11])      