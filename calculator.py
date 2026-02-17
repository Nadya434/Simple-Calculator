import math

def add(a, b):
    """
    Складывает два числа.
    
    Args:
        a (float): Первое слагаемое
        b (float): Второе слагаемое
        
    Returns:
        float: Сумма a и b
        
    Example:
        >>> add(5, 3)
        8
    """
    return a + b

def subtract(a, b):
    """
    Вычитает второе число из первого.
    
    Args:
        a (float): Уменьшаемое
        b (float): Вычитаемое
        
    Returns:
        float: Разность a и b
        
    Example:
        >>> subtract(10, 4)
        6
    """
    return a - b

def multiply(a, b):
    """
    Умножает два числа.
    
    Args:
        a (float): Первый множитель
        b (float): Второй множитель
        
    Returns:
        float: Произведение a и b
        
    Example:
        >>> multiply(6, 7)
        42
    """
    return a * b

def divide(a, b):
    """
    Делит первое число на второе.
    
    Args:
        a (float): Делимое
        b (float): Делитель
        
    Returns:
        float or str: Результат деления или сообщение об ошибке
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(10, 0)
        'Ошибка: деление на ноль!'
    """
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    """
    Возводит число в степень.
    
    Args:
        a (float): Основание
        b (float): Показатель степени
        
    Returns:
        float: Результат возведения в степень
        
    Example:
        >>> power(2, 3)
        8
    """
    return a ** b

def mod(a, b):
    """
    Возвращает остаток от деления.
    
    Args:
        a (float): Делимое
        b (float): Делитель
        
    Returns:
        float or str: Остаток от деления или сообщение об ошибке
        
    Example:
        >>> mod(10, 3)
        1
        >>> mod(10, 0)
        'Ошибка: деление на ноль!'
    """
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a % b

def square_root(a):
    """
    Вычисляет квадратный корень числа.
    
    Args:
        a (float): Число для извлечения корня
        
    Returns:
        float or str: Квадратный корень или сообщение об ошибке
        
    Example:
        >>> square_root(16)
        4.0
        >>> square_root(-4)
        'Ошибка: нельзя извлечь корень из отрицательного числа!'
    """
    if a < 0:
        return "Ошибка: нельзя извлечь корень из отрицательного числа!"
    return math.sqrt(a)

def calculate():
    """
    Основная функция калькулятора с пользовательским интерфейсом.
    
    Выводит меню, получает ввод от пользователя и выполняет выбранную операцию.
    После каждой операции спрашивает, хочет ли пользователь продолжить.
    """
    while True:
        print("\n" + "="*40)
        print("ПРОСТОЙ КАЛЬКУЛЯТОР v1.0")
        print("="*40)
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Остаток от деления")
        print("7. Квадратный корень")
        print("0. Выход")
        print("="*40)
        
        choice = input("Выберите операцию (0-7): ")
        
        # Выход из программы
        if choice == "0":
            print("\nСпасибо за использование калькулятора! До свидания!")
            break
        
        # Проверка корректности выбора
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nОшибка: неверный выбор! Пожалуйста, выберите 0-7.")
            input("\nНажмите Enter, чтобы продолжить...")
            continue
        
        try:
            # Для всех операций кроме корня нужно 2 числа
            if choice == "7":
                a = float(input("Введите число: "))
                b = None  # не используется для корня
            else:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
        except ValueError:
            print("\nОшибка: введите числа! Используйте точку для дробных (например, 3.14)")
            input("\nНажмите Enter, чтобы продолжить...")
            continue
        
        # Выполнение операции
        print("\n" + "-"*40)
        if choice == "1":
            result = add(a, b)
            print(f"Результат: {a} + {b} = {result}")
        elif choice == "2":
            result = subtract(a, b)
            print(f"Результат: {a} - {b} = {result}")
        elif choice == "3":
            result = multiply(a, b)
            print(f"Результат: {a} * {b} = {result}")
        elif choice == "4":
            result = divide(a, b)
            if isinstance(result, str):
                print(f"Результат: {result}")
            else:
                print(f"Результат: {a} / {b} = {result}")
        elif choice == "5":
            result = power(a, b)
            print(f"Результат: {a} ^ {b} = {result}")
        elif choice == "6":
            result = mod(a, b)
            if isinstance(result, str):
                print(f"Результат: {result}")
            else:
                print(f"Результат: {a} % {b} = {result}")
        elif choice == "7":
            result = square_root(a)
            if isinstance(result, str):
                print(f"Результат: {result}")
            else:
                print(f"Результат: √{a} = {result}")
        print("-"*40)
        
        # Спрашиваем, хочет ли пользователь продолжить
        print()
        cont = input("Хотите выполнить другую операцию? (д/н): ").lower()
        if cont not in ["д", "y", "yes", "да", "lf"]:
            print("\nСпасибо за использование калькулятора! До свидания!")
            break

if __name__ == "__main__":
    calculate()
