#!/usr/bin/python3

import sys, json, os.path, random, shutil, os
from pprint import pprint

def load(file):                    #Открывает файл json для чтения
	with open(file, 'r') as g:
		return json.load(g)

def write_f(data_new, file):       #Открывает файл json из предыдущей функции для записи
	data = load(file)
	with open(file, 'w') as f:
		data.update(data_new)
		json.dump(data, f, ensure_ascii=False, indent = 2)

def write_fu(file, words):        #Сохраняет файл в котором добавляется score
		with open(file, 'w') as f1:
			json.dump(words,f1, ensure_ascii=False, indent = 2)

#Рандомный режим

def randommod(filewords, file_name):
	for key in filewords.keys():
				random_key = random.choice(list(filewords))
				if filewords[random_key]["score"] <= 0:
					print(filewords[random_key]["score"], random_key, end = '')
					if filewords[random_key]["translation"] == input('-'):
						filewords[random_key]["score"] += 1
						print('+')
						write_fu(file_name, filewords)
					else:
						print('Ответ:', filewords[random_key]["translation"])
				else:
					pass

#Линейный режим

def linemode(filewords, file_name):
	for key in filewords.keys():
		if filewords[key]["score"] <= 0:
			print(key, end = '')
			otvet = input('-')
			if filewords[key]["translation"] == otvet:
				filewords[key]["score"] += 1
				print('+')
				write_fu(file_name, filewords)
			else:
				print('Ответ:', filewords[key]["translation"])
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

#Для перезаписи json файлов

def rewrite(filename1, filename2):
	with open(filename1, 'r') as f:
		data = json.load(f)
		with open(filename2, 'w') as g:
			json.dump(data, g, ensure_ascii=False, indent = 2)

# rewrite("wor.json", 'wor2.json')