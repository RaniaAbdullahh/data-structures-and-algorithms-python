def binary_search(list, x):
    min_num = 0
    max_num = len(list)-1
    mid = (max_num + min_num)//2

    if not len(list):
        return - 1
    while(list[mid] != x):
        if(min_num > max_num):
            return -1
        elif(list[mid] > x):
            max_num = mid - 1
        elif(list[mid] < x):
            min_num = mid + 1
        mid = (max_num + min_num)//2

    return mid

#print(binary_search([20], 20))