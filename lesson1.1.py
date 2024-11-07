# while True:
#     print("Выберите операцию:")
#     print("1. Сложение")
#     print("2. Вычитание")
#     print("3. Умножение")
#     print("4. Деление")
#     print("5. Выход")
#
#     choice = input("Введите номер операции (1/2/3/4/5): ")
#
#     if choice == '5':
#         print("Калькулятор завершен.")
#         break
#
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
#
#     if choice == '1':
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif choice == '2':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif choice == '3':
#         print(f"{num1} * {num2} = {num1 * num2}")
#     elif choice == '4':
#         if num2 != 0:
#             print(f"{num1} / {num2} = {num1 / num2}")
#         else:
#             print("Ошибка: деление на ноль")
#     else:
#         print("Некорректный ввод")
