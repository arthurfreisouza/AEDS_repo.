import sys

days_ = int(input())
number_ = int(input())
cond1 = (1 <= days_ <= 100000)
cond2 = (1 <= number_ <= 1000000)

if cond1 == False or cond2 == False:
    sys.exit()

arr = str(input()).split(" ")
arr = list(map(int, arr))
print(arr)
sum_result = 0
count = 0
arr2 = []
index_list = []
for index, value in enumerate(arr):
    sum_result = sum_result + int(value)
    if sum_result == number_:
        index_list.append(index)
        sum_result = 0
print(index_list)

initial = 0 
final = None

for i in index_list:
    final = index_list
    for j in range(int(initial), int(final), 1):
        count = count + 1
        if index_list[j] != "0":
            initial = final
            break
