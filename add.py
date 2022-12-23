#!/usr/bin/python3

import sys, argparse


def createParser ():
	parser = argparse.ArgumentParser()
	parser.add_argument ('-a', '--name', default='мир')
	parser.add_argument ('-l' "=", '--lastname', default='мир')
	return parser

parser_new = createParser()
namespace = parser_new.parse_args(sys.argv[1:])
namespace = parser_new.parse_args(sys.argv[1:])
# print (namespace)

print ("your name,", str(namespace.name))
print ("your lastname, {}!".format (namespace.lastname) )

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