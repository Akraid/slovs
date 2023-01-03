#!/usr/bin/python3

import sys, json, os.path, random, shutil, os

#Открывает файл json для чтения

def load_file(file):
	with open(file, 'r') as g:
		return json.load(g)

#Открывает файл json из предыдущей функции для записи (используется для добавления слов в словарь)

def update_file(data_new, file):
	data = load_file(file)
	with open(file, 'w') as f:
		data.update(data_new)
		json.dump(data, f, ensure_ascii=False, indent = 2)

#Сохраняет файл в котором добавляется score

def write_fu(file, words):
		with open(file, 'w') as f1:
			json.dump(words,f1, ensure_ascii=False, indent = 2)

#Выполнение сравнения в режиме 1 и 2 (рндом/линия)
def doprint(filewords, keys, file_name):
	if filewords[keys]["score"] <= 0:
		print('')
		print(filewords[keys]["score"], keys, end = '')
		otvet = input('-')
		if filewords[keys]["translation"] == otvet:
			filewords[keys]["score"] += 1
			print('+')
			write_fu(file_name, filewords)
		else:
			print('Ответ:', filewords[keys]["translation"])
	else:
		 pass

#Перебор очков во всем словаре words (1)

def scors(filewords):
	scors_list = []
	for k, v in filewords.items():
		scors = v['score']
		scors_list.append(v['score'])
	if min(scors_list) == 1:
		return scors_list
	else:
		return scors_list

#Рандомный режим

def randommod(filewords, file_name):
	random_key = keys, values = random.choice(list(filewords.items()))
	doprint(filewords, keys, file_name)

#Линейный режим

def linemode(filewords, file_name):
	for keys in filewords.keys():
		doprint(filewords, keys, file_name)
	
#Перебор очков во всем словаре words (для остановки цикла при условии min(scors_list) != 1 )

def scors(filewords):
	scors_list = []
	for k, v in filewords.items():
		scors = v['score']
		scors_list.append(v['score'])
	if min(scors_list) == 1:
		return scors_list
	else:
		return scors_list

#Для перезаписи json файлов

def rewrite(filename1, filename2):
	with open(filename1, 'r') as f:
		data = json.load(f)
		with open(filename2, 'w') as g:
			json.dump(data, g, ensure_ascii=False, indent = 2)
