def factorial_function(number_, show_ = False):
    factorial_expression = ''
    factorial_number_ = 1
    for i in range(int(number_), 1, - 1):
        factorial_number_ = factorial_number_ * i
        factorial_expression = str(factorial_expression + '{} x '.format(i))
    factorial_expression = str(factorial_expression + '1')

    if show_ == True:
        print(2 * '\n')
        print(' Calculating factorial : {} = {}'. format(factorial_expression, factorial_number_))
    else:
        print(2 * '\n')
        print('The factorial of {} is : {}'.format(number_,factorial_number_))



    print(1 * '\n')
    print(' Loading ... ')
    print(1 * '\n')