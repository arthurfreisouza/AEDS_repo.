def Validate(function_):
    def validate(number_):
        if number_ < 0:
            raise Exception('This value is not right ... ')
        else:
            return function_(number_)
    return validate



@Validate
def function_Exercise(number_) -> list:
    lst = []
    for i in range(number_):
        print(i)
        count = 0
        for j in range(1, int(i / 2) + 1):
            if (i % j == 0):
                count = count + 1  
        if (count == 1):
            lst.append(int(i))
    return lst


number = int(input('Write a number here : '))

my_list = []

my_list = function_Exercise(number)

sum = 0

for i in my_list:
    sum = sum + i

print(' The sum of the prime values {} until the number {} is {}. '.format(my_list, number, sum))

