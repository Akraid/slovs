#!/usr/bin/python3

words = {}

f = open('zadanie.txt')
for i in f:
	z = i.split("-")
	words[z[0][:-1]] = z[1][1:-1]

print('''
                        ВЫБЕРИТЕ РЕЖИМ: 
                                                        
"1" Для рандомнго режима               "2" Для последовательного режима''')

vibor = int(input())

j = 0

if vibor == 1:
	import random
	for key in words.keys():
		random_key = random.choice(list(words))
		print(random_key, end = '')
		if words[random_key] == input('-'):
			print('+')
			j += 1
		else:
			print('Ответ:', words[random_key])

if vibor == 2:
	for key in words.keys():
		print(key, end = '')
		otvet = input('-')
		if words[key] == otvet:
			print('+')
		else:
			print('Ответ:', words[key])

print(j,'из 70 повторений')

