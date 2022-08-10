def mergeSort(list_a):
    n = len(list_a)

    if n <= 1:
      return 
    pivot = n // 2

    left = list_a[:pivot]
    right = list_a[pivot:]
    
    mergeSort(left) 
    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        list_a[k] = left[i]
        i += 1
      else:
        list_a[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      list_a[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      list_a[k] = right[j]
      j += 1
      k += 1 

