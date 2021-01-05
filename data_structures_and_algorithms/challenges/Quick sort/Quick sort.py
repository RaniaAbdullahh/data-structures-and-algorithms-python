def quickSort(arr, left, right): 
    if left < right: # 0 < 5 
        # print(left,right)
        pivot = partition(arr, left, right) 
        # print (arr)
      
        # print(left, pivot-1)
        quickSort(arr, left, pivot-1)
     
        quickSort(arr, pivot+1, right)
       
    return arr
def partition(arr, left, right): 
    i = (left-1) 
    pivot = arr[right] # pivot=15
    for j in range(left, right):
        if arr[j] <= pivot: 
            i = i+1
            # print(arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1] 
    return (i+1) 
    
if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    print(quickSort(arr, 0, len(arr)-1) )