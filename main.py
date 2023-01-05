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
			cli.cli_f()
		case '-u':
			cli.cli_u()
		case '-r':
			cli.cli_r()
		case '-l':
			cli.cli_l()
		case '-d':
			cli.cli_d()
		case _:
			cli.cli_eror()
			exit(1)

cli.check_file()

print("ВЫБЕРИТЕ РЕЖИМ:".center(shutil.get_terminal_size().columns))
print('"1" Для рандомнго режима', end = '' )
print('"2" Для последовательного режима'.rjust(shutil.get_terminal_size().columns - len('"1" Для рандомнго режима')))

vibor = int(input())

match vibor:
	case 1:
			cli.randommod()
	case 2:
			cli.linemode()
	case _:
		print('Нужно выбрать 1 или 2')
print('Обновите словарь')
