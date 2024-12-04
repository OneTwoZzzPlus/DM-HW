class InvalidInput(Exception):
    pass


clear = lambda x: x.replace('\t', '').replace('\r', '').replace('\n', '')

msg = '''Эта программа строит полином Жегалкина булевой функции, заданной по таблице истинности.

Введите последовательность из 0 и 1 длиной, кратной степени 2.
Например > 10010110

Или путь к файлу (его название, если он лежит в той же директории) "в кавычках".
Например > "./path/to/file.txt"
Или так > "file.txt"

Введите текст после > затем нажмите enter, а случае ошибки, повторите ввод.

Для выхода введите q, для справки введите h.'''


if __name__ == '__main__':
    print(msg)
    while 1:
        try:
            # Ввод, убираем пробелы по краям, пустые символы
            print('\nВведите ТИ или путь к файлу')
            s = input(' > ').strip(' ')
            s = clear(s)
            if s == 'q':
                exit(0)
            if s == 'h':
                print(msg)  
                break
            
            # Читаем файл
            if len(s) > 2:
                if s[0] == '"' and s[-1] == '"':
                    with open(s.strip('"'), 'r', encoding='utf-8') as file:
                        s = clear(file.read())
                    
            # Проверяем корректность ТИ
            s = s.replace(' ', '')
            for x in s:
                if x not in '01':
                    raise InvalidInput(
                        f'Некорректный символ в таблице истинности: "{x}"!')

            # Проверяем длину последовательности
            n = len(s)
            if not (n > 0 and (n & (n-1)) == 0):
                raise InvalidInput(f'ТИ неправильной длины: {n}, '
                                    'необходима натуральная степень 2')
            
            # Производим рассчёт
            result = "0 + 1x + 0y + 1xy"
            
            # Вывод на экран
            print("Результат:")
            print(result)
            
            # Сохранение
            print('\nНажмите enter, чтобы выйти или '
                  'введите путь к файлу для сохранения')
            while 1:
                s = clear(input('Сохранить: '))
                if s == '':
                    break
                try:
                    file = open(s.strip('"'), 'w', encoding='utf-8')
                    file.write(result)
                    file.close()
                    break
                except PermissionError:
                    print('Недостаточно прав для сохранения!')
                except (FileNotFoundError, FileExistsError):
                    print('Такой файл нельзя создать!')
                    
            exit(0)
        except KeyboardInterrupt:
            print('Выход по системному прерыванию!')
            exit(0)
        except PermissionError:
            print('Недостаточно прав для работы с файлом!')
        except (FileNotFoundError, FileExistsError):
            print('Такого файла не существует!')
        except UnicodeDecodeError:
            print('Некорректный символ!')
        except InvalidInput as e:
            print(e)
        