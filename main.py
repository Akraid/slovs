#!/usr/bin/python3

import sys, json, os.path, random

x = len(sys.argv)

if x == 3 and str(sys.argv[1]) == '-f':
	check_file = os.path.exists(sys.argv[2])

if x == 3 and str(sys.argv[1]) == '-f' and check_file:

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

	print(j,'из 70 повторений')

elif x == 3 and str(sys.argv[1]) == '-f' and not check_fiel:
	print('Нет такого файла')
else:
	print('Ошибка, как надо вводить:"./main -f name_file"')
