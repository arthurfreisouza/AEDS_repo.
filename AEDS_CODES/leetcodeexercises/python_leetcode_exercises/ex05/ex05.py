import area_module
length = float(input(' Write the length here.'))
weigth = float(input(' Write the weigth here.'))

area = float(area_module.area_function(length, weigth))


print(" This area is : {}".format(area))