import os
import tempfile
import argparse
import json
from pprint import pprint

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')
    parser.add_argument('-v', '--val')
    args = parser.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if not os.path.isfile(storage_path):
        with open(storage_path, 'w'):
            pass

    data = {}
    with open(storage_path, 'r') as f:
        if os.path.getsize(storage_path) > 0:
            data = json.load(f)

    if args.val:
        with open(storage_path, 'w') as f:
            new_val = [args.val]
            if args.key in data:
                new_val = data[args.key]
                if new_val.count(args.val) == 0:
                    new_val.append(args.val)
            data[args.key] = new_val
            f.write(json.dumps(data))
    else:
        if args.key in data:
            print(', '.join(data[args.key]))


if __name__ == '__main__':
    main()


'''
На этой неделе мы с вами реализуем собственный key-value storage. Вашей задачей будет написать скрипт, который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).

Запись значения по ключу

> storage.py --key key_name --val value

Получение значения по ключу

> storage.py --key key_name

Ответом в данном случае будет вывод с помощью print соответствующего значения

> value

или

> value_1, value_2

если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке их добавления. Обратите внимание на пробел после запятой.

Если значений по ключу не было найдено, выводите пустую строку или None.

Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей будет считать аргументы, переданные вашей программе, и записать соответствующую пару ключ-значение в файл хранилища или вывести значения, если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json. Проверьте добавление нескольких ключей и разных значений.

Файл следует создавать с помощью модуля tempfile.


1
2
3
4
5
6
import os
import tempfile
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
  ...
Создайте скрипт хранилища и загрузите его на платформу.
'''