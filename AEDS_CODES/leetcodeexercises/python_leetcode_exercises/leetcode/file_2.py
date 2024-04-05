lst_ = []
values = []
number = int(input(" Write the length : "))
lst_numbers = str(input(" Write the list of numbers : "))
lst_ = lst_numbers.split(" ")
var = None
for i in range(0, len(lst_)):
    var = 0
    for j in range(i, len(lst_)):
        if lst_[i] == lst_[j]:
            var = var + 1
        else:
            values.append(var)
            break
    i = i + var

print(max(values))
    


    