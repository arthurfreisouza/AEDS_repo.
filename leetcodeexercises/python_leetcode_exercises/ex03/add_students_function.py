def add_students():
    students = []
    while True:
        value = str(input('Write the name of the students.'))
        if value == 'x':
            print('Stopping to add students in the list')
            break
        students.append(value)
    return students

