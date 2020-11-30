 

def insertShiftArray(arr,add):
 
    if type(arr) != list:
        return 'Invalid Input'
    if type(add) != int:
         return 'Invalid Input'   
    midpoint = len(arr)//2+1
    if len(arr)%2 ==0:
        return arr[:len(arr)//2] + [add] + arr[len(arr)//2:]
    else:
         return arr[0:midpoint] + [add] + arr[midpoint:]   

