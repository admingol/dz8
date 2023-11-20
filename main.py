import time
import logging

# Налаштування логування
logging.basicConfig(filename='timing.log', level=logging.INFO)

def timing(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time

    # Запис інформації у журнал
    logging.info(f"Функція '{func.__name__}' виконана за {execution_time} секунд")

    return result, execution_time

def example_function():
    time.sleep(2)

# Виклик функції timing для вимірювання часу виконання example_function
result, execution_time = timing(example_function)

# Виведення результатів на консоль
print(f"Результат: {result}")
print(f"Час виконання: {execution_time} секунд")

