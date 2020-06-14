import os

directory = input("Введите путь к файлу: ")  # Вводится путь к файлу и записывается в переменную Name
print("Подтвердите путь", directory)  # Выводит просьбу подтвердить путь
input("Нажмите Enter для продолжения")  # Заставляет прогу ждать ввода Enter
if os.path.exists(directory):
    files = os.listdir(directory)
    tree = os.walk(directory)
    for d in tree:
        print(d)
else:
    print("Файл или директория не существует")
