number1 = float(input('Enter a number: '))
operator = input('Enter an operator ("+", "-", "*", "/", "pow", "div", "mod"): ')
number2 = float(input('Enter a number: '))

if (number2 == 0) and ((operator == "/") or (operator == "div") or (operator == "mod")):
    print('Division by zero!')
elif operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "pow":
    print(number1 ** number2)
elif operator == "div":
    print(number1 // number2)
elif operator == "mod":
    print(number1 % number2)
else:
    print('Unknown operator!')
