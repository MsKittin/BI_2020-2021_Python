a = float(input())
op = input()
b = float(input())

if (b == 0) and ((op == "/") or (op == "div") or (op == "mod")):
    print("Деление на 0!")
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "pow":
    print(a ** b)
elif op == "div":
    print(a // b)
elif op == "mod":
    print(a % b)
else:
    print("Неизвестная операция!")