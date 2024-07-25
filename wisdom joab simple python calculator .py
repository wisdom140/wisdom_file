# Get user inputs
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operator = input('Enter the operator (+, -, *, /): ')

# Perform calculation based on the operator
if operator == '+':
  result = num1 + num2
elif operator == '-':
  result = num1 - num2
elif operator == '*':
  result = num1 * num2
elif operator == '/':
  if num2 == 0:
    print('Error: Cannot divide by zero.')
  else:
    result = num1 / num2
else:
  print('Invalid operator.')
  
def display(result_text, result):
  print(f'{result_text}: {result}')


# Print the result (if valid)
if operator in ('+', '-', '*', '/'):
  display('Result:', float(result))