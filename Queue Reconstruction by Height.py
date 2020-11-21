def minMoves2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    def quicksort(arr, left, right):

        mid = div(arr, left, right)
        if mid>left+1:
            quicksort(arr, left, mid - 1)
        if mid<right-1:
            quicksort(arr, mid + 1, right)

    def div(arr, left, right):
        base = arr[left]
        while left < right:
            while left < right and arr[right] >= base:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] < base:
                left += 1
            arr[right] = arr[left]

        arr[left] = base
        return left

    quicksort(nums, 0, len(nums) - 1)

    midind = len(nums) // 2
    midnum = nums[midind]
    res = sum(nums[midind + 1:]) - sum(nums[0:midind]) + (2 * midind - len(nums) + 1) * midnum
    return res

nums=[1,4,6,7]
print(minMoves2(nums))