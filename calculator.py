def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

if __name__ == "__main__":
    print("Калькулятор готов к работе!")
