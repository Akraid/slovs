#!/usr/bin/python3

import sys, json, os.path, random

x = len(sys.argv)

if x != 3 or str(sys.argv[1]) != '-f':
	print('Ошибка, надо вводить:"./main.py -f name_file.json')
	exit(1)

if not os.path.exists(sys.argv[2]):
	print('Файла ', sys.argv[2], 'не существует')
	exit(1)

file_name_new = sys.argv[2]
with open(file_name_new, 'r') as g:
	wor_new = json.load(g)

print('                          ВЫБЕРИТЕ РЕЖИМ:')
print('"1" Для рандомнго режима', '                 ', end = '' )
print('"2" Для последовательного режима')

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
