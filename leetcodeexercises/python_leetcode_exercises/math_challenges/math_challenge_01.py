import sys

args = sys.argv



def remove_and_join_lines(file_):
    with open(file_, 'r') as file:
        content = file.read()

    # Substituir quebras de linha por nada, unindo as linhas
    content_without_newlines = content.replace('\n', '')

    with open(file_, 'w') as file:
        file.write(content_without_newlines)


remove_and_join_lines(args[1])
with open(args[1], 'r') as file:
    new_content = str(file.read())
sum_result = 0
for i in range(100):
    sum_result = sum_result + int(new_content[i])


print(' The sum is {}'.format(sum_result))

for i in range(len(str(sum_result)) - 10, len(str(sum_result)), -1):
    print(sum_result[i])


value = '3710728753390210279879799822083759024651013574025046376937677490009712648124896970078050417018260538'

sum_result_2 = 0

for i in range(len(value)):
    sum_result_2 = sum_result_2 + int(value[i])

print(sum_result_2)