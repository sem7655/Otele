password1 = 1053
password2 = 1010

input_password = int(input("Введите пароль: "))

if input_password == password1 or input_password == password2:
    print("Дверь открыта")
else:
    print("Доступ запрещен")
