lst = [1, 2, 3, 4, 7, 8, 9]

def insertShiftArray(arr,val):
    if len(arr)%2==0:
        return arr[:len(arr)//2] + [val] + arr[len(arr)//2:]  
    else:
        return arr[:len(arr)//2+1] + [val] + arr[len(arr)//2+1:]  
        
    

print(insertShiftArray(lst,11))
