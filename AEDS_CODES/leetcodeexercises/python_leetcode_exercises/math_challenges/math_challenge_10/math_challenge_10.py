import sys

def Function_Challenge() -> tuple:
    args = sys.argv
    with open('/home/arthur/Desktop/{}'.format(args[1]), 'r') as my_file:
        file_subject = my_file.read()
    lst = []

    for num in file_subject.split():
        try:
            lst.append(int(num))
        except:
            print(' This value is not right !')

    count_pair = 0
    count_odd = 0
    for i in lst:
        if len(str(i)) == 1:
            count_odd = count_odd + 1
        elif len(str(i)) == 2:
            count_pair = count_pair + 1
        elif len(str(i)) == 3:
            count_odd = count_odd + 1
        elif len(str(i)) == 4:
            count_pair = count_pair + 1
        else:
            raise Exception(' This value is not right ... ')
    return (count_pair, count_odd)

my_tuple = ()
my_tuple = Function_Challenge()

print(' There are {} numbers with pair digits and {} numbers with odd digits'.format(my_tuple[0], my_tuple[1]))