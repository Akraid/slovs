#!/usr/bin/python3

import sys, json, os.path, random, shutil, os
import myclasses as cl 

try:
	file_name = os.environ['SLOVSFILE']
except KeyError:
	print('Переменная окружения SLOVSFILE не найдена')
	exit(1)

cli = cl.CommandLineInterface(file_name)

if len(sys.argv) > 1:
	match sys.argv[1]:
		case '-f':
			file_name = sys.argv[2]
			cli.c_fn(file_name)
		case '-u':
			data_argv = sys.argv[2].split("=")
			data_new = {data_argv[0]:dict(translation = data_argv[1], score = 0)}
			cli.c_d(data_new)
			cli.update_file()
			print('Word', '"{}"'.format(data_argv[0]), 'with meaning', '"{}"'.format(data_argv[1]), 'successfully added')
			exit()
		case '-r':
			file_name = sys.argv[2]
			fu.rewrite("base.json", file_name)
			exit()
		case '-l':
			cli.list()
		case '-d':
			words = cli.load_file()
			cli.c_f(words)
			words.pop(sys.argv[2])
			cli.write_fu()
			exit()
		case _:
			print("Ошибка, надо вводить:./main.py -f name_file.json для открытия файла\n"
				"Ошибка, надо вводить:./main.py -u name_file.json для добавления слова\n"
			"Ошибка, надо вводить:./main.py -r name_file.json для сброса словаря к базовым значениям")
			exit(1)

cli.check_file()

print("ВЫБЕРИТЕ РЕЖИМ:".center(shutil.get_terminal_size().columns))
print('"1" Для рандомнго режима', end = '' )
print('"2" Для последовательного режима'.rjust(shutil.get_terminal_size().columns - len('"1" Для рандомнго режима')))

vibor = int(input())

words = cli.load_file()
cli.c_fw(words)
scors_list = cli.scors()

match vibor:
	case 1:
		while min(scors_list) != 1:
			cli.randommod()
			scors_list = cli.scors()
	case 2:
		while min(scors_list) != 1:
			cli.linemode()
			scors_list = cli.scors()
	case _:
		print('Нужно выбрать 1 или 2')
print('Обновите словарь')
