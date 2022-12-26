#!/usr/bin/python3

import sys, argparse, json
from pprint import pprint

new_data = {"world" : "мир", 'book' : 'книга'}

def write(data, filename):
	data = json.dumps(data)
	data = json.loads(str(data))
	with open(filename, 'r+', encoding = 'utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent = 2)

write(new_data, 'wor2.json')

# def read(filename):
# 	with open(filename, 'r', encoding = 'utf-8') as f:
# 		return json.load(f)

# perezapis = read('wor.json')
# write(perezapis, 'wor2.json')

# def greet(name):
# 	result = f'Hello {name}'
# 	print(result)

# greet('oleg')
# greet('world')


# def createParser ():
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument ('-a', '--name', default='мир')
# 	parser.add_argument ('-l' "=", '--lastname', default='мир')
# 	return parser

# parser_new = createParser()
# namespace = parser_new.parse_args(sys.argv[1:])
# namespace = parser_new.parse_args(sys.argv[1:])
# # print (namespace)

# print ("your name,", str(namespace.name))
# print ("your lastname, {}!".format (namespace.lastname) )

# slovr = dict()

# slovr.update(str(namespace.name))

# print (slovr)




# SLOVSFILE=WOR.JSON ./main.py  
# ./main.py -f wor.json
# ./main.py -a world=мира

# Задание 1 Перевести программу на библеатеку argparse
# Задание 2 Добавить в программу аргумент -a который выведит принт 
# Задание 3 Добавить в программу аргумент -a который добавит слово в файл словаря

# сделать копию json!!!!