def caching_fibonacci():
    cache = {}  # Створення порожнього кешу

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевірка, чи число є у кеші
            return cache[n]
        else:
            # Рекурсивний виклик для обчислення числа Фібоначчі
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result  # Збереження результату в кеші
            return result

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610


