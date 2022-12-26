#!/usr/bin/python3

import sys, json, os.path, random, shutil, os, argparse

try:
	file_name = os.environ['SLOVSFILE']
except KeyError:
	print('Переменная окружения SLOVSFILE не найдена')
	exit(1)

if len(sys.argv) > 1:
	match sys.argv[1]:
		case '-f':
			file_name = str(sys.argv[2])
		case '-a':
			try:
				def write(data, filename):
					with open(filename, 'r+', encoding = 'utf-8') as f:
						data = json.load(f)
						data.update(data_new)
						f.seek(0)
						json.dump(data, f, ensure_ascii=False, indent = 2)

				data_argv = sys.argv[2].split("=")
				data_new = {data_argv[0] : data_argv[1]}
				
				write(data_new, "wor3.json")
				print('Word', '"{}"'.format(data_argv[0]), 'with meaning', '"{}"'.format(data_argv[1]), 'successfully added')
				exit()
			except ValueError:
				print("Can't add new word! Please enter the command as follows: python3 main.py -a apple=яблоко")
				exit(1)
		case _:
			print('Ошибка, надо вводить:"./main.py -f name_file.json')
			exit(1)

if not os.path.exists(file_name):
	print('Файла ', file_name, 'не существует')
	exit(1)

with open(file_name, 'r') as g:
	wor_new = json.load(g)

print("ВЫБЕРИТЕ РЕЖИМ:".center(shutil.get_terminal_size().columns))
print('"1" Для рандомнго режима', end = '' )
print('"2" Для последовательного режима'.rjust(shutil.get_terminal_size().columns - len('"1" Для рандомнго режима')))

vibor = int(input())

j = 0

match vibor:
	case 1:
		for key in wor_new.keys():
			random_key = random.choice(list(wor_new))
			print(random_key, end = '')
			if wor_new[random_key] == input('-'):
				print('+')
				j += 1
			else:
				print('Ответ:', wor_new[random_key])
	case 2:
		for key in wor_new.keys():
			print(key, end = '')
			otvet = input('-')
			if wor_new[key] == otvet:
				print('+')
			else:
				print('Ответ:', wor_new[key])
	case _:
		print('Нужно выбрать 1 или 2')

print(j,'из', len(wor_new.keys()))
