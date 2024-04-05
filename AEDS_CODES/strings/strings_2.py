word = str(input("Write yout word."))

lst_ = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
translated_num = ""
for char in word:
    if char.isnumeric() != True and char != "-":
        if char in lst_[0]:
            translated_num = translated_num + '2'
        elif char in lst_[1]:
            translated_num = translated_num + '3'
        elif char in lst_[2]:
            translated_num = translated_num + '4'
        elif char in lst_[3]:
            translated_num = translated_num + '5'
        elif char in lst_[4]:
            translated_num = translated_num + '6'
        elif char in lst_[5]:
            translated_num = translated_num + '7'
        elif char in lst_[6]:
            translated_num = translated_num + '8'
        elif char in lst_[7]:
            translated_num = translated_num + '9'
    else:
        translated_num = translated_num + char

print(translated_num)