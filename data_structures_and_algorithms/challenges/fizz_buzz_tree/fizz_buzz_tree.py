def fizzbuzzTree (tree):
    arr=[]

    for i in tree :
        arr.append(i)
    for index,i in enumerate(arr):

        if i % 3 == 0 and i % 5 == 0:
            arr[index]= 'FizzBuzz'
            

        elif i % 3 == 0:
            arr[index]='Fizz'
           
        
        elif i % 5 == 0:
            arr[index]= 'Buzz'
            
        else:
            arr[index] = str(i)
    
    return arr





if __name__ == "__main__":
   print(fizzbuzzTree ([3,15,21,30,4,8])) 