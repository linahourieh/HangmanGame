def binarySearch(list,start,end,element):
  
  
  
  if end>=start:
    middle=(start+end)//2
    #print(middle)
    if list[middle]==element:
      return True
    elif list[middle]>element:
      return binarySearch(list,start,middle-1,element)
    else:
      return binarySearch(list,middle+1,end,element)
  else:
    return False  

#print(binarySearch(list_key,0,len(list_key)-1," "))    
