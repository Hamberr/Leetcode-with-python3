def binary_search(list, item):
    
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        if list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

list = [1, 2, 8, 7, 9]
print(binary_search(list, 2))
#return 1
