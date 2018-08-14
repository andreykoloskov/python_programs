import tempfile
import os

class File:
    def __init__(self, filepath):
        self.filepath = filepath
        self.f = open(filepath, 'w+')

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()

    def write(self, line):
        self.f.write(line)

    def __add__(self, obj):
        new_obj = File(tempfile.gettempdir() + '/' + self.filepath.split('/')[-1])
        self.f.seek(0)
        obj.f.seek(0)
        new_obj.write(self.f.read() + obj.f.read())
        new_obj.f.seek(0)
        return  new_obj

    def __iter__(self):
        return self

    def __next__(self):
        line = self.f.readline()
        if not line:
            raise StopIteration

        return line

    def __str__(self):
        return self.filepath


if __name__ == '__main__':
    first = File('/Users/andreykoloskov/Documents/msu/prac/python_programs/python_mailru/course_1/task8/text1.txt')
    second = File('/Users/andreykoloskov/Documents/msu/prac/python_programs/python_mailru/course_1/task8/text2.txt')
    first.write('line1\n')
    second.write('line2\n')

    new_obj = first + second
    print(new_obj)

    for line in new_obj:
        print(line)

'''
В этом задании вам нужно создать интерфейс для работы с файлами. Класс File должен поддерживать несколько необычных операций.

Класс инициализируется полным путем.


1
obj = File('/tmp/file.txt')
Класс должен поддерживать метод write.


1
obj.write('line\n')
Объекты типа File должны поддерживать сложение.


1
2
3
4
first = File('/tmp/first')
second = File('/tmp/second')
new_obj = first + second
В этом случае создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.

Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.


1
2
for line in File('/tmp/file.txt'):
  ...
И наконец, при выводе файла с помощью функции print должен печататься его полный путь, переданный при инициализации.


1
2
3
4
obj = File('/tmp/file.txt')
print(obj)
'/tmp/file.txt'
Опишите свой класс в скрипте и загрузите на платформу.
'''

'''
import os
import uuid


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, obj):
        new_path = os.path.join(
            os.path.dirname(self.path),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())

        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line

'''