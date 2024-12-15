# Завдання 1

# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії.
# Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

# Ваше завдання - розробити функцію total_salary(path),
# яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

# Вимоги до завдання:

# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


# Рекомендації для виконання:

# Використовуйте менеджер контексту with для читання файлів.
# Пам'ятайте про встановлення кодування при відкриті файлів
# Для розділення даних у кожному рядку можна застосувати метод split(',').
# Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
# Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.

def total_salary(path:str)->tuple:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
            total = 0
            for line in lines:
                total += int(line.split(',')[1])
                
        if not lines:
            return (0, 0)  
        
        average = total / len(lines)
        return (total, average)
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

# Приклад використання
total, average = total_salary("task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
