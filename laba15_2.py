import subprocess


def task_manager_win():
    while True:
        cmd = input('\n введите команду (list,run,kill,exit) :').lower()

        if cmd == 'exit':
            break

        elif cmd == 'list':
            subprocess.run(['tasklist'])

        elif cmd == 'run':
            app = input(' Название приложения : ')
            try:
                subprocess.Popen(app, shell=True)
            except FileNotFoundError:
                print("Ошибка")

        elif cmd == 'kill':
            target = input ('Имя (calc)')
            if not target.lower().endswith('.exe'):
                target += '.exe'
                res = subprocess.run(['taskkill', '/F','/IM', target], capture_output=True, shell= True)


task_manager_win()