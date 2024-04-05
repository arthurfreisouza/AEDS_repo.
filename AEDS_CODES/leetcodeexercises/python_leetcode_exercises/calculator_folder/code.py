import sys
from calculator_module import Calculator

args = sys.argv
print(args)
object_1 = Calculator(args[1], float(args[2]), float(args[3]))