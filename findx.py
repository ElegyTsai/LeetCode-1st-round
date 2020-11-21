def removeKdigits( num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if k == len(num) or len(num) == 0:
        return "0"
    arr = list(num)
    n = 0
    while k > 0:
        if k==len(arr)-n:
            arr[n:]=[]
            break
        m = min(arr[n:n + k+1])
        i = arr[n:].index(m)

        if i == 0:
            n = n + 1
        else:
            arr[n:n+i] = []
            k = k - i
            n = n + 1
        print(arr)

    num = "".join(arr)
    return num


s="43214321"
k=4
removeKdigits(s,k)