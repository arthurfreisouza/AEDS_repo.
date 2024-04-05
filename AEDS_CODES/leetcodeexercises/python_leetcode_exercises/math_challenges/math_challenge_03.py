def Validate(function_):
    def validate(num_):
        if int(num_) < 0:
            raise Exception(' This value is not right.')
        else:
            return function_(num_)
    return validate

@Validate
def fourth(num_ : int) -> int:
    return num_ ** 4

@Validate
def fifth(num_ : int) -> int:
    return num_ ** 5

lst = []
total_sum = 0
play_button = str(input('Write fourth or fifth : '))
for i in range(1000000):
    sum_result = 0
    for digit_str in str(i):
        digit = int(digit_str)
        if play_button == 'fourth':
            sum_result = sum_result + fourth(digit)

        elif play_button == 'fifth':
            sum_result = sum_result + fifth(digit)

        else:
            raise Exception(' The option is not right.')
        
    if (int(sum_result) == int(i) and int(sum_result) != 1 and int(sum_result) != 0):
        lst.append(sum_result)
        total_sum = total_sum + int(sum_result)
        print(sum_result)

print(' The sum of the numbers {} is {}. '.format(lst, total_sum))


        
