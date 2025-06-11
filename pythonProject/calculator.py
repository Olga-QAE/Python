def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a % b

def calculator():
    operations = {
        "1": ("Сложение", add),
        "2": ("Вычитание", subtract),
        "3": ("Умножение", multiply),
        "4": ("Деление", divide),
        "5": ("Возведение в степень", power),
        "6": ("Остаток от деления", modulo),
        "0": ("Выход", None)
    }

    while True:
        print("\nПростой калькулятор")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        choice = input("Выберите операцию (0-6): ")
        if choice == "0":
            print("Выход из программы. До свидания!")
            break
        if choice not in operations:
            print("Неверный выбор. Попробуйте снова.")
            continue
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введено не число.")
            continue

        op_name, func = operations[choice]
        result = func(a, b)
        print(f"Результат {op_name.lower()} {a} и {b} = {result}")

if __name__ == "__main__":
    calculator()
