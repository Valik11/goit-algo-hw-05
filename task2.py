import re
from typing import Callable

def generator_numbers(text: str):
    # Шукаємо всі дійсні числа у тексті за допомогою регулярного виразу
    pattern = r'(?<=\s)\d+\.\d+(?=\s)'  # Шаблон для дійсного числа
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо знайдене дійсне число як float

def sum_profit(text: str, func: Callable):
    # Використовуємо переданий генератор для знаходження дійсних чисел
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
