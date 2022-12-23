#!/usr/bin/python3

import sys, json, os.path, random, shutil, os, argparse

try:
	file_name = os.environ['SLOVSFILE']
except KeyError:
	print('Переменная окружения SLOVSFILE не найдена')
	exit(1)

if len(sys.argv) > 1:
	if str(sys.argv[1]) == '-f':
		file_name = str(sys.argv[2])
	if str(sys.argv[1]) == '-a':
		new_data = {str(sys.argv[2].split("=")[0]) : str(sys.argv[2].split("=")[1])}
		with open('wor.json', 'r+', encoding = 'utf-8') as f:
			data = json.load(f)
			data.update(new_data)
			f.seek(0)
			json.dump(data, f, ensure_ascii=False, indent = 2)
			exit()
	else:
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
