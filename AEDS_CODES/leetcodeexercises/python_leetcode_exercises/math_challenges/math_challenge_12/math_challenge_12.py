from itertools import combinations

def All_Combinations(arr, n) -> list:
    return list(combinations(arr, n))

def Inverting_Order(arr) -> list:
    return sorted(arr, reverse=True)

def find_zero_sum_groups(arr, n):
    if len(arr) == 0:
        return 'No elements to combine'
    
    returned_value = All_Combinations(arr, n)
    array_to_return = []

    for i in returned_value:
        if sum(i) == 0:
            array_to_return.append(Inverting_Order(i))

    if not array_to_return:
        return 'No combinations'
    
    return array_to_return
