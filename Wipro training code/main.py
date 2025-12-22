from calculators.add import add
from calculators.sub import subtract
from calculators.mul import multiply
from calculators.div import divide

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
