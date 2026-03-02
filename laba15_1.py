import os
import datetime
def file_manager():
    print('список комманд: \n create (создание файла) \n delete (удаление файла) \n read (чтение файла) \n edit (добавление текста) \n seфrch (поиск файла) \n exit(остановка программы) ')
    while True:
        command = input('Введите команду ').strip().lower()

        if command == 'exit':
            break

        elif command == 'create':
            filename = input ('Введите имя файла ')
            try:
                #'x' создает файл, если он уже есть то ошибка
                with open (filename, 'x', encoding='utf-8') as f:
                    pass
                print(f'файл {filename} создан')
            except FileExistsError:
                print("Ошибка, файл уже существует")

        elif command == 'delete':
            filename = input ('введите имя файла для удаления ')
            #проверка является ли обьект файлом и существует ли по указанному пути
            if os.path.exists(filename) and os.path.isfile(filename):
                os.remove(filename)
                print(f'Файл {filename} удален')
            else:
                print('Файл не найден или это директория')

        elif command == 'read':
            filename = input ('Введите имя файла ')
            try:
                with open (filename, 'r', encoding='utf-8') as f:
                    print('Содержание файла:')
                    print(f.read())
            except FileNotFoundError:
                print('Файл не существует')
            except IsADirectoryError:
                print('это директория а не файл')

        elif command == 'edit':
            filename = input ('Введите имя файла ')
            text = input('Введите текст для добавления ')
            try:
                with open (filename, 'a', encoding='utf-8') as f:
                    f.write(text + '\n')
                    print('текст успешно добавлен')
            except FileNotFoundError:
                print('Ошибка файл не найден ')

        elif command == 'search':
            path = input ('Где искать? Введите . для текущей папки ')
            query = input('введите часть названия или расширения ').lower()
            for root, dirs, files in os.walk(path): #ходит по каждой подпапке
                for file in files:
                    if query in file.lower():
                        full_path = os.path.join(root, file)
                        stats = os.stat(full_path)
                        size = stats.st_size
                        #превращаем строку типа float в datetime
                        mtime = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
                        print(f'{file} | {size:} | {mtime}')
file_manager()