import subprocess
def ip_scanner():
    print ('Сканер айпи адресов')
    ip_range = input('введите диапазон айпи (например 192.168.0.1 - 192.169.0.5').strip()
    try:
        start_ip,end_ip = ip_range.split('-')
        ip_parts = start_ip.split('.')
        base_ip = '.'.join(ip_parts[:-1])+'.'
        start_num = int(ip_parts[-1])
        end_num = int(end_ip.split('.')[-1])
        active_hosts=[]
        for i in range (start_num,end_num+1):
            ip = base_ip+str(i)
            #n - чтобы винд запрашивал 1 пакета не 4, ждем ответ 200 мс
            res =subprocess.run(['ping','-n','1','-w','200',ip],capture_output=True)
            # если 0 то ответ получили
            if res.returncode == 0:
                print(f'{ip} - answer')
            else:
                print(f'{ip} - error')
    except Exception as e:
        print(f'ошибка в формате {e}')
ip_scanner()