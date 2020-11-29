def reverse_array(arr):
    """Reverses a list
    Args:
        arr (list): python list
    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    i = len(arr) - 1 
    result=[]
    while i >= 0 :
        result.append(arr[i])
        i -= 1
    print(result)
    return result



reverse_array([1,2,3,4])
