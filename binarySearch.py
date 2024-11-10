def sort(a):
    n = len(a)
    i = 1
    while i < n: 
        j = i -1 
        current = a[i]
        while j >= 0 and a[j] > current: 
            a[j+1] = a[j]
            j = j - 1 
        a[j+1] = current
        i += 1
    return a 





def bsa(target,arr):
    left = 0 
    right = len(arr) - 1 
    while left <= right: 
        mid = (left +(right- left))//2 
        if arr[mid] == target: 
            return mid
        elif target< arr[mid]: 
            right = mid - 1
        else: 
            left = mid + 1 
    return -1 



    