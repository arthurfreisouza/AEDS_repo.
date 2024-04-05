import counter

print('Welcome to this program.')
while True:
    start = int(input('Write the value to start. \n'))
    end = int(input('Write the value to finish. \n'))
    step = int(input('Write the step value. \n'))
    counter.count(start, end, step)
    continue_var = str(input( 'Press c to continue or x to exit. \n'))

    if continue_var == 'x':
        break
