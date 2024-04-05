def count(start, end, step):
    aux_count_1 = 0
    aux_count_2 = 0
    aux_count_3 = 0
    for i in range(start, end + 1, 1):
        print('x[{}] = {}'.format(int(aux_count_1), int(i)))
        aux_count_1 = aux_count_1 + 1
    print(5 * '\n')
    for i in range(start, end + 1, 2):
        print('x[{}] = {}'.format(int(aux_count_2), int(i)))
        aux_count_2 = aux_count_2 + 1
    print(5 * '\n')    
    for i in range(start, end + 1, step):
        print('x[{}] = {}'.format(int(aux_count_3), int(i)))
        aux_count_3 = aux_count_3 + 1
