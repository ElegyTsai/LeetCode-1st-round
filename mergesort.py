def mergesort(arr):
    def merge(arr1,arr2):
        res=[]
        i=0
        j=0
        while i<len(arr1) or j <len(arr2):
            if i<len(arr1) and j <len(arr2):
                if arr1[i]>arr2[j]:
                    res.append(arr2[j])
                    j +=1
                else:
                    res.append(arr1[i])
                    i += 1
            elif j==len(arr2):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        return res

    def mymergesort(arr):
        n=len(arr)
        if n>=2:
            mid=n//2
            arr1=mymergesort(arr[0:mid])
            arr2=mymergesort(arr[mid:])
            return merge(arr1, arr2)
        else:
            return arr
    return mymergesort(arr)

a=[4,68,1,23,57,8]
print(mergesort(a))