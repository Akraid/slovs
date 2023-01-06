#!/usr/bin/python3

import sys, json, os.path, random, shutil, os

class Slovsfile():
	__file_name = None
	filewords = None

	def setfilename(self, file_arg):
		self.__file_name = file_arg

	def getfilename(self):
		return self.__file_name 

	#Проверка на наличие файла

	def check(self):
		if not os.path.exists(self.__file_name):
			print('Файла ', self.__file_name, 'не существует!')
			exit(1)

#Открыть файл для чтения (привязываем к переменной)

	def load(self):
		with open(self.__file_name, 'r') as g:
			return json.load(g)

#1.Если дефолтного файла нет, то создаёт его. 2. Открывает и перезаписывает файл

	def update(self, data_new):
		data = {}
		if os.path.exists(self.__file_name):
			data = self.load()
		with open(self.__file_name, 'w') as f:
			data.update(data_new)
			json.dump(data, f, ensure_ascii=False, indent = 2)

	def write(self):
			with open(self.getfilename(), 'w') as f1:
				json.dump(self.filewords, f1, ensure_ascii=False, indent = 2)

#-----------------------------------------------------------------------------------------------------------------------------------------

class CommandLineInterface(Slovsfile):

	def __init__(self):
		try:
			self.setfilename(os.environ['SLOVSFILE'])
		except KeyError:
			print('Переменная окружения SLOVSFILE не найдена')
			exit(1)

	def file(self, file_arg):
		"""для ключа -f"""
		self.setfilename(file_arg)
		self.filewords = self.load()

	def update(self):
		"""для ключа -u"""
		data_argv = sys.argv[2].split("=")
		data_new = {data_argv[0]:dict(translation = data_argv[1], score = 0)}
		super().update(data_new)
		print('Word', '"{}"'.format(data_argv[0]), 'with meaning', '"{}"'.format(data_argv[1]), 'successfully added')
		exit()

	def reset(self):
		"""для ключа -r"""
		if len(sys.argv) == 3 and os.path.exists(sys.argv[2]):
			self.__file_name = sys.argv[2]
		file_scan = self.load()
		for k, v in file_scan.items():
			v['score'] = 0
		self.filewords = file_scan
		self.write()
		exit()

	def list(self):
		"""для ключа -l"""
		table = self.load()
		print("Word Translation Score")
		for k, v in table.items():
			print(k, v["translation"], v["score"])
		exit()

	def delete(self):
		"""для ключа -d"""
		file_scan = self.load()
		file_scan.pop(sys.argv[2])
		self.filewords = file_scan
		self.write()
		exit()

	def error(self):
		"""для ключа error"""
		print("Ошибка, надо вводить:./main.py -f name_file.json для открытия файла\n"
			"Ошибка, надо вводить:./main.py -u key=ключ для добавления слова в словарь\n"
			"Ошибка, надо вводить:./main.py -r name_file.json для сброса очков в выбраном файле\n"
			"Ошибка, надо вводить:./main.py -l показать словарь\n"
			"Ошибка, надо вводить:./main.py -d key для удаления слова из словаря")
		exit(1)

#-----------------------------------------------------------------------------------------------------------------------------------------

class Gamewords(Slovsfile):
	scores_list = None

	def __init__(self, file_arg):
		self.setfilename(file_arg)
		self.scores_list = self.scores()

  #Принт выбора режима

	@staticmethod
	def print_vibor():
		print("ВЫБЕРИТЕ РЕЖИМ:".center(shutil.get_terminal_size().columns))
		print('"1" Для рандомнго режима', end = '' )
		print('"2" Для последовательного режима'.rjust(shutil.get_terminal_size().columns - len('"1" Для рандомнго режима')))

	#Перебор очков во всем словаре

	def scores(self):
		self.filewords = self.load()
		scores_list = []
		f = self.filewords
		for k, v in f.items():
			scores = v['score']
			scores_list.append(v['score'])
		if min(scores_list) == 1:
			return scores_list
		else:
			return scores_list

	#Рандомный режим

	def randommod(self):
		while min(self.scores_list) != 1:
			self.scores_list = self.scores()
			random_key = keys, values = random.choice(list(self.filewords.items()))
			self.doprint(keys)

	#Линейный режим

	def linemode(self):
		while min(self.scores_list) != 1:
			self.scores_list = self.scores()
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
				self.write()
			else:
				print('Ответ:', fw[keys]["translation"])
		else:
			 pass

#------------------------------------------------------------------------------------------------------------------------------------------
