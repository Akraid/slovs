#!/usr/bin/python3

import json
import sys

words = {}

x = str(sys.argv[1])

if x == '-f':
	p = str(sys.argv[2])
	f = open(p)
	for i in f:
		z = i.split("-")
		words[z[0][:-1]] = z[1][1:-1]

	fiel_name = 'wor.json'
	with open(fiel_name, 'w', encoding = 'utf-8') as g:
		json.dump(words, g, ensure_ascii = False)

	fiel_name_new = 'wor.json'
	with open(fiel_name_new, 'r') as g:
		wor_new = json.load(g)
	print(wor_new)

	print('''
	                        ВЫБЕРИТЕ РЕЖИМ: 
	                                                        
	"1" Для рандомнго режима               "2" Для последовательного режима''')

	vibor = int(input())

	j = 0

	if vibor == 1:
		import random
		for key in wor_new.keys():
			random_key = random.choice(list(wor_new))
			print(random_key, end = '')
			if wor_new[random_key] == input('-'):
				print('+')
				j += 1
			else:
				print('Ответ:', wor_new[random_key])

	if vibor == 2:
		for key in wor_new.keys():
			print(key, end = '')
			otvet = input('-')
			if wor_new[key] == otvet:
				print('+')
			else:
				print('Ответ:', wor_new[key])

	print(j,'из 70 повторений')