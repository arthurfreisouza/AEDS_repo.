import add_students_function
import sort_function


print(' Welcome to this program. Here we will create a list of students. \n')
my_students_list = []
my_students_list = add_students_function.add_students()

random_name = sort_function.random_choice(my_students_list)


print(' The chosen name is {}'.format(random_name))
