import add_students_function
import ordened_function


print(' Welcome to this program. Here we will create a list of students. \n')
my_students_list = []
my_students_list = add_students_function.add_students()
print(my_students_list)

list_orderned = []
list_orderned = ordened_function.ordened_func(my_students_list)


print(' The list ordened is {}'.format(list_orderned))
