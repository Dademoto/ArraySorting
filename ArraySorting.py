#array sorting usando il .sort

array = [8586,8658,468,465,8496]
def sort(array):
    iterations=0
    for i in range(len(array)- 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                x = array[i]
                array[i] = array[j]
                array[j] = x
            iterations+=1
    return iterations
iterations=sort(array)
print(array, "It took" ,iterations, "iterations to sort the array" )