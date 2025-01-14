def partition(lst, start, end):
    pos = start                          
    for i in range(start, end):           
        if lst[i] < lst[end]:             
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos] 
                                          
    return pos

def quick_sort_recursive(lst, start, end):
    if start < end:                       
        pos = partition(lst, start, end)
        quick_sort_recursive(lst, start, pos - 1)
        quick_sort_recursive(lst, pos + 1, end)
        

array_esempio = [-1, 200, 23, 34, 9999999, 100, -99, 1, 0]
array_sistemato = quick_sort_recursive(array_esempio, 0, len(array_esempio)-1)
print("Array ricorsivamente ordinato: " + str(array_esempio))