def do_operation(a, b, code):
    match code:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/": return a // b


first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))
code = input("Введите знак операции (+-*/):")
print("Результат:", do_operation(first, second, code))
