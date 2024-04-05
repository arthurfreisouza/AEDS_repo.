def Validate(function_):
    def validate(number_):
        if number_ >= 0:
            return function_(number_)
        else:
            raise Exception('Its not a positive number ...')
    return validate

@Validate
def Number_Function(number_ : int) -> list:
    lst_to_return = []
    for i in range(int((number_ / 2)) + 1, 0, -1):
        count = 0
        if (number_ % i == 0):
            for j in range(1, int((i / 2)) + 1):
                if (i % j == 0):
                    count = count + 1
            if (count == 1):
                lst_to_return.append(int(i))
                print(i)

    return lst_to_return

