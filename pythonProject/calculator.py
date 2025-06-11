def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a % b

def calculator():
    operations = {
        "1": ("Додавання", add),
        "2": ("Віднімання", subtract),
        "3": ("Множення", multiply),
        "4": ("Ділення", divide),
        "5": ("Піднесення до степеня", power),
        "6": ("Залишок від ділення", modulo),
        "0": ("Вихід", None)
    }

    while True:
        print("\nПростий калькулятор")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        choice = input("Оберіть операцію (0–6): ")
        if choice == "0":
            print("Вихід з програми. До побачення!")
            break
        if choice not in operations:
            print("Неправильний вибір. Спробуйте ще раз.")
            continue
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: введено не число.")
            continue

        op_name, func = operations[choice]
        result = func(a, b)
        print(f"Результат {op_name.lower()} {a} та {b} = {result}")

if __name__ == "__main__":
    calculator()