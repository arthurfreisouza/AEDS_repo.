def readint_function():
    '''
        You will stay in this loop until you digit a int number and you will put it in the list.
    '''
    while True:
        try:
            number_ = int(input( 'Write something here : '))
        except ValueError:
            print('Its not an integer number. ')
        else:
            print('{} is an integer number. '.format(number_))
            return number_

