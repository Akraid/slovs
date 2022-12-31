#!/usr/bin/python3

import sys, json, os.path, random, shutil, os
import myfunctions as fu

try:
	file_name = os.environ['SLOVSFILE']
except KeyError:
	print('Переменная окружения SLOVSFILE не найдена')
	exit(1)

if len(sys.argv) > 1:
	match sys.argv[1]:
		case '-f':
			file_name = sys.argv[2]
		case '-u':
			try:
				data_argv = sys.argv[2].split("=")
				data_new = {data_argv[0]:dict(translation = data_argv[1], score = 0)}
				fu.update_file(data_new, file_name)
				print('Word', '"{}"'.format(data_argv[0]), 'with meaning', '"{}"'.format(data_argv[1]), 'successfully added')
				exit()
			except ValueError:
				print("Can't add new word! Please enter the command as follows: python3 main.py -u apple=яблоко")
				exit(1)
		case '-r':
			file_name = sys.argv[2]
			fu.rewrite("base.json", file_name)
			exit()
		case _:
			print("Ошибка, надо вводить:./main.py -f name_file.json для открытия файла\n"
				"Ошибка, надо вводить:./main.py -u name_file.json для добавления слова\n"
			"Ошибка, надо вводить:./main.py -r name_file.json для сброса словаря к базовым значениям")
			exit(1)

if not os.path.exists(file_name):
	print('Файла ', file_name, 'не существует')
	exit(1)

print("ВЫБЕРИТЕ РЕЖИМ:".center(shutil.get_terminal_size().columns))
print('"1" Для рандомнго режима', end = '' )
print('"2" Для последовательного режима'.rjust(shutil.get_terminal_size().columns - len('"1" Для рандомнго режима')))

vibor = int(input())

words = fu.load_file(file_name)
scors_list = fu.scors(words)

match vibor:
	case 1:
		while min(scors_list) != 1:
			fu.randommod(words, file_name)
			scors_list = fu.scors(words)
	case 2:
		while min(scors_list) != 1:
			fu.linemode(words, file_name)
			scors_list = fu.scors(words)
	case _:
		print('Нужно выбрать 1 или 2')
print('Обновите словарь')
