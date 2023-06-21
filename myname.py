# Получение имени и фамилии от пользователя
first_name = input("Пожалуйста, введите ваше имя: ")
last_name = input("Пожалуйста, введите вашу фамилию: ")

# Запись имени и фамилии в файл
with open('output.txt', 'w') as f:
    f.write(f"Имя: {first_name}\n")
    f.write(f"Фамилия: {last_name}\n")

print("Имя и фамилия успешно записаны в файл 'output.txt'.")
