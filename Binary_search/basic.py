"""
二分查找的适用条件是有序列表~
最基本的二分查找，返回列表中目标值item的索引，若没有则返回None.
注意while循环的条件是low<=high，这是由于判断是否存在某一元素实际上是通过list[mid]判断的，
当low = high - 1时，mid = low = high - 1，判断的实际是list[low]若item = list[high]，则程序进入low = low + 1，此时low == high
若while循环条件是low < high，则跳出循环返回None，即搜索不到list[high]

由于是查找item是否存在，因此若list[mid]不是，那么不必管它，因此low和high的更新分别为mid + 1和mid - 1
"""
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
