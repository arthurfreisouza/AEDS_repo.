def int32_to_ip(int32 : str):
    number = str(int32)
    my_list = number.split('.')
    my_list = list(map(lambda x : int(x, 2), my_list))
    for i in my_list:
        i = str(i)
    my_string = '.'.join(my_list)
    return my_string

