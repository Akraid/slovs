#!/usr/bin/python3

import sys, json, os.path, random, shutil, os 
import functionspy as fu

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
				functions.write_f(data_new, file_name)
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

print("ВЫБЕРИТЕ РЕЖИМ:".center(shutil.get_terminal_size().columns))
print('"1" Для рандомнго режима', end = '' )
print('"2" Для последовательного режима'.rjust(shutil.get_terminal_size().columns - len('"1" Для рандомнго режима')))

vibor = int(input())

words = fu.loadw(file_name)

match vibor:
	case 1:
		for key in words.keys():
			random_key = random.choice(list(words))
			print(random_key, end = '')
			if words[random_key]["translation"] == input('-'):
				words[random_key]["score"] += 1
				print('+')
				test2.j += 1
			else:
				print('Ответ:', words[random_key]["translation"])
	case 2:
		for key in words.keys():
			print(key, end = '')
			otvet = input('-')
			if words[key]["translation"] == otvet:
				print('+')
			else:
				print('Ответ:', words[key]["translation"])
	case _:
		print('Нужно выбрать 1 или 2')

print(j,'из', len(words.keys()))
