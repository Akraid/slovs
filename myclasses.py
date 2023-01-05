#!/usr/bin/python3

import sys, json, os.path, random, shutil, os
from pprint import pprint

class CommandLineInterface():
	file_name = None
	filewords = None
	data_new = None
	scors_list = None

	def __init__(self, file_path):
		self.file_name = file_path
		self.filewords = self.load_file()
		self.scors_list = self.scors()
#-----------------------------------------------------------------------------------------------------------------------------------------

#Проверка на наличие дефолтного файла

	def check_file(self):
		if not os.path.exists(self.file_name):
			print('Файла ', self.file_name, 'не существует!')
			exit(1)

#Открыть файл для чтения (привязываем к переменной)

	def load_file(self):
		with open(self.file_name, 'r') as g:
			return json.load(g)

#1.Если дефолтного файла нет, то создаёт его. 2. Открывает и перезаписывает файл

	def update_file(self):
		data = {}
		if os.path.exists(self.file_name):
			data = self.load_file()
		with open(self.file_name, 'w') as f:
			data.update(self.data_new)
			json.dump(data, f, ensure_ascii=False, indent = 2)

#-----------------------------------------------------------------------------------------------------------------------------------------

	#Перебор очков во всем словаре

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
		while min(self.scors_list) != 1:
			self.scors_list = self.scors()
			random_key = keys, values = random.choice(list(self.filewords.items()))
			self.doprint(keys)

	#Линейный режим

	def linemode(self):
		while min(self.scors_list) != 1:
			self.scors_list = self.scors()
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

#------------------------------------------------------------------------------------------------------------------------------------------

	def cli_f(self):
		"""для ключа -f"""
		self.file_name = sys.argv[2]
		self.filewords = self.load_file()

	def cli_u(self):
		"""для ключа -u"""
		data_argv = sys.argv[2].split("=")
		self.data_new = {data_argv[0]:dict(translation = data_argv[1], score = 0)}
		self.update_file()
		print('Word', '"{}"'.format(data_argv[0]), 'with meaning', '"{}"'.format(data_argv[1]), 'successfully added')
		exit()

	def cli_r(self):
		"""для ключа -r"""
		if len(sys.argv) == 3 and os.path.exists(sys.argv[2]):
			self.file_name = sys.argv[2]
		file_scan = self.load_file()
		for k, v in file_scan.items():
			v['score'] = 0
		self.filewords = file_scan
		self.write_fu()
		exit()

	def cli_l(self):
		"""для ключа -l"""
		table = self.load_file()
		print("Word Translation Score")
		for k, v in table.items():
			print(k, v["translation"], v["score"])
		exit()

	def cli_d(self):
		"""для ключа -d"""
		file_scan = self.load_file()
		file_scan.pop(sys.argv[2])
		self.filewords = file_scan
		self.write_fu()
		exit()

	def cli_eror(self):
		"""для ключа eror"""
		print("Ошибка, надо вводить:./main.py -f name_file.json для открытия файла\n"
			"Ошибка, надо вводить:./main.py -u key=ключ для добавления слова в словарь\n"
			"Ошибка, надо вводить:./main.py -r name_file.json для сброса очков в выбраном файле\n"
			"Ошибка, надо вводить:./main.py -l показать словарь\n"
			"Ошибка, надо вводить:./main.py -d key для удаления слова из словаря")
		exit()	
