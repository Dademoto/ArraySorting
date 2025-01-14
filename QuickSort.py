def partition(array, min, max):
    metà = array[max] #inizialmente come metà
    i = min - 1

    for j in range(min, max):
        if array[j] <= metà:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[max] = array[max], array[i+1]
    return i+1

def quicksort(array, min=0, max=None):
    if max is None:
        max = len(array) - 1

    if min < max:
        posizione_metà = partition(array, min, max)
        quicksort(array, min, posizione_metà-1)
        quicksort(array, posizione_metà+1, max)

my_array = [-1, 34, 25, 12, 22, 11, 90, 9999]
quicksort(my_array)
print("Sorted array:", my_array)