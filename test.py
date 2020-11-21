
arr = [-10,]  # 列表头不使用


def addNum(arr, num):
    """
    :type num: int
    :rtype: None
    """
    if len(arr) == 1:
        arr.append(num)
    else:
        i = 1
        while i < len(arr):

            if arr[i] > num:
                break
            i += 1
        arr.insert(i, num)



addNum(arr,1)
addNum(arr,10)
addNum(arr,1)
addNum(arr,12)
addNum(arr,2)

for i in range(len(arr)):
    print(arr[i])