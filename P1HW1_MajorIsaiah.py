# Isaiah Major
# October 31, 2026
# P1HW1 - Mathematical Expressions
# This program calculates an exponent and performs
# addition and subtraction using user-entered integers.

print("----- Calculating Exponents -----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()
print(f"{base} raised to the power of {exponent} is {result} !!")

print()
print("----- Addition and Subtraction -----")

first_num = int(input("Enter a starting integer: "))
second_num = int(input("Enter an integer to add: "))
third_num = int(input("Enter an integer to subtract: "))

sum_result = first_num + second_num
final_result = sum_result - third_num

print()
print(f"{first_num} + {second_num} = {sum_result}")
print(f"{sum_result} - {third_num} = {final_result}")