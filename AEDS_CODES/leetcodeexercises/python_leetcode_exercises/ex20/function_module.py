def media_function(lst_):
    sum = 0
    for i in lst_:
        sum = sum + i
    media_result = float(sum / len(lst_))
    return media_result


def bigger_function(lst_):
    aux_bigger = 0
    for i in range(len(lst_)):
        if lst_[i] > lst_[aux_bigger]:
            aux_bigger = i
    return lst_[aux_bigger]


def lower_function(lst_):
    aux_lower = 0
    for i in range(len(lst_)):
        if lst_[i] < lst_[aux_lower]:
            aux_lower = i
    return lst_[aux_lower]
        
        