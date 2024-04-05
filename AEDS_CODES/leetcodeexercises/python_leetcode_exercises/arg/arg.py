import sys

arguments = sys.argv

print(arguments)

for i in sys.argv:
    if i.lower() == 'arthur':
        print(' You are Arthur !')
        