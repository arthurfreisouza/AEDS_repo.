#from module_ import return_float, return_strin
#
#str_val = input("Type a string value ...")
#num_val = input("Type a float value ... ")
#
#a = return_strin(str_val)
#b = return_float(num_val)
#print(a)
#print(b)

###############################################################

#lst_ = []
#
#try:
#    val_1 = float(input("Type a string value ..."))
#    val_2 = float(input("Type a float value ... "))
#    lst_.append(val_1)
#    lst_.append(val_2)
#    result = lst_[0] / lst_[1]
#
#except ValueError:
#    pass
#except ZeroDivisionError:
#    pass
#except IndexError:
#    pass
#except KeyboardInterrupt:
#    pass





#######################################################################

my_dic = {}
while True:
    try:
        my_string = str(input(" What is your name ..."))
        my_value = int(input(" Type your result ..."))

    except Exception as error:
        print(f" The error is : {error}")

    my_dic[my_string] = my_value
    
    if my_string == "q":
        break


print(" Writing on file ...")

for key,value in my_dic.items():
    with ("/home/arthur/Desktop/thrash_file.txt", "w") as thrash_f:
        word = str(key) + " : " + str(value)
        thrash_f.write(word)

with ("/home/arthur/Desktop/thrash_file.txt", "r") as thrash_f:
       for lines in thrash_f:
           print(lines)