# 1. Чётное или нечётное
# num1 = int(input("Введите число для проверки на чётность: "))
# if num1 % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")

# 2. Положительное, отрицательное или ноль
# num2 = float(input("Введите число для проверки знака: "))
# if num2 > 0:
#     print("Положительное")
# elif num2 < 0:
#     print("Отрицательное")
# else:
#     print("Ноль")

# 3. Возрастной доступ
# age = int(input("Введите ваш возраст: "))
# if age >= 18:
#     print("Доступ разрешён")
# else:
#     print("Доступ запрещён")

# 4. Максимум из двух чисел
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# if a > b:
#     print(f"Максимум: {a}")
# else:
#     print(f"Максимум: {b}")

# 5. Проверка пароля
# password_secret = "python123"
# user_input = input("Введите пароль: ")
# if user_input == password_secret:
#     print("Пароль верный")
# else:
#     print("Неверный пароль")

# 6. Максимум из трёх чисел
# n1 = float(input("Число 1: "))
# n2 = float(input("Число 2: "))
# n3 = float(input("Число 3: "))
# if n1 >= n2 and n1 >= n3:
#     print(f"Наибольшее: {n1}")
# elif n2 >= n1 and n2 >= n3:
#     print(f"Наибольшее: {n2}")
# else:
#     print(f"Наибольшее: {n3}")

# 7. Оценка по баллам
# score = int(input("Введите баллы (0-100): "))
# if 90 <= score <= 100:
#     print("A")
# elif 70 <= score <= 89:
#     print("B")
# elif 50 <= score <= 69:
#     print("C")
# elif score < 50:
#     print("F")

# 8. Делимость числа (FizzBuzz)
# fb_num = int(input("Введите число для FizzBuzz: "))
# if fb_num % 3 == 0 and fb_num % 5 == 0:
#     print("FizzBuzz")
# elif fb_num % 3 == 0:
#     print("Fizz")
# elif fb_num % 5 == 0:
#     print("Buzz")
# else:
#     print(fb_num)

# 9. Координатная плоскость
# x = float(input("Введите x: "))
# y = float(input("Введите y: "))
# if x > 0 and y > 0:
#     print("I четверть")
# elif x < 0 and y > 0:
#     print("II четверть")
# elif x < 0 and y < 0:
#     print("III четверть")
# elif x > 0 and y < 0:
#     print("IV четверть")
# else:
#     print("Точка на оси")

# 10. Тип треугольника
# side1 = float(input("Сторона 1: "))
# side2 = float(input("Сторона 2: "))
# side3 = float(input("Сторона 3: "))
# if side1 == side2 == side3:
#     print("Равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")
