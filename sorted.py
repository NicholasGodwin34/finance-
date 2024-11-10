def sort(a): 
    n = len(a) # n is the number of elements in the array 
    i = 1  # initialize i as 1 
    while i < n: # while i is les than the number of elements
        j = i -1  # j is the index just before i 
        current = a[i] # this is the element in index i 
    while j >= 0 and a[j] > current:  # while index j >= 0 and element at index j > than the one in index i 
        a[j+ 1] = a[j]  # 
        j = j-1
    a[j+ 1] = current
    i += 1

    return a 

