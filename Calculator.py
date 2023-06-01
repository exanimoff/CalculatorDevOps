def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Простой консольный калькулятор.")
print("Доступные операции: +, -, *, /")

while True:
    operation = input("Выберите операцию (+, -, *, /) или введите 'q' для выхода: ")

    if operation == 'q':
        print("Выход из калькулятора")
        break

    if operation not in ['+', '-', '*', '/']:
        print("Неверная операция. Попробуйте еще раз.")
        continue

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    print("Результат: ", result)
