def bubble_sort(arr : list[int]):
    size_arr = len(arr)
    for i in range(size_arr):
        for j in range(i + 1, size_arr):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


def normal_bubble_sort(arr : list[int]):
    size_arr = len(arr)
    for i in range(size_arr):
        for j in range(0, size_arr - 1 - i): # Irei varrer do 0 até a penúltima posição disponível...
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(bubble_sort([10, 90, 33, 4]))
print(normal_bubble_sort([10, 90, 33, 4]))















#==
def reverse_bubble_sort(arr : list[int]):
    size_arr = len(arr)
    for i in range(size_arr):
        for j in range(i + 1, size_arr):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def reverse_normal_bubble_sort(arr : list[int]):
    size_arr = len(arr)
    for i in range(size_arr):
        for j in range(0, size_arr - 1 - i): # Irei varrer do 0 até a penúltima posição disponível...
            if arr[j] < arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(reverse_bubble_sort([10, 90, 33, 4]))
print(reverse_normal_bubble_sort([10, 90, 33, 4]))