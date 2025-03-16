def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        return "Ошибка. Деление на ноль недопустимо."
    return x / y

print("Доступные операции:")
print("1 - Сложение")
print("2 - Вычитание")
print("3 - Умножение")
print("4 - Деление")

user_choice = input("Пожалуйста, введите номер необходимой операции: ")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if user_choice == "1":
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif user_choice == "2":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif user_choice == "3":
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif user_choice == "4":
    print(f"{num1} / {num2} = {divide(num1, num2)}")