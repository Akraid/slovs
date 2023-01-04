#!/usr/bin/python3

import sys, json, os.path, random, shutil, os

class CommandLineInterface():
	file_name = None
	filewords = None
	data_new = None

	def __init__(self, file_path):
		self.file_name = file_path

	def c_d(self, data_new):
		self.data_new = data_new
		return self.data_new

	def c_fw(self, words):
		self.filewords = words
		return self.filewords

	def c_fn(self, file_name):
		self.file_name = file_name
		return self.file_name

	def check_file(self):
		if not os.path.exists(self.file_name):
			print('Файла ', self.file_name, 'не существует!')
			exit(1)

	def load_file(self):
		with open(self.file_name, 'r') as g:
			return json.load(g)

	def list(self):
		table = self.load_file()
		print("Word Translation Score")
		for k, v in table.items():
			print(k, v["translation"], v["score"])
		exit()

	def update_file(self):
		data = {}
		if os.path.exists(self.file_name):
			data = self.load_file()
		with open(self.file_name, 'w') as f:
			data.update(self.data_new)
			json.dump(data, f, ensure_ascii=False, indent = 2)

	#Перебор очков во всем словаре words (1)

	def scors(self):
		scors_list = []
		f = self.filewords
		for k, v in f.items():
			scors = v['score']
			scors_list.append(v['score'])
		if min(scors_list) == 1:
			return scors_list
		else:
			return scors_list

	#Рандомный режим

	def randommod(self):
		random_key = keys, values = random.choice(list(self.filewords.items()))
		self.doprint(keys)

	#Линейный режим

	def linemode(self):
		for keys in self.filewords.keys():
			self.doprint(keys)

	#Выполнение сравнения в режиме 1 и 2 (рндом/линия)

	def doprint(self, keys):
		fw = self.filewords
		if fw[keys]["score"] <= 0:
			print('')
			print(fw[keys]["score"], keys, end = '')
			otvet = input('-')
			if fw[keys]["translation"] == otvet:
				fw[keys]["score"] += 1
				print('+')
				self.write_fu()
			else:
				print('Ответ:', fw[keys]["translation"])
		else:
			 pass

	#Сохраняет файл в котором добавляется score

	def write_fu(self):
			with open(self.file_name, 'w') as f1:
				json.dump(self.filewords, f1, ensure_ascii=False, indent = 2)
