#!/usr/bin/python3

import sys
import argparse


def createParser ():
	parser = argparse.ArgumentParser()
	parser.add_argument ('-n', '--name', default='мир')
	parser.add_argument ('-l', '--lastname', default='мир')

	return parser

parser_new = createParser()
namespace = parser_new.parse_args(sys.argv[1:])

# print (namespace)

print ("your name,", namespace.name)
print ("your lastname, {}!".format (namespace.lastname) )


# SLOVSFILE=WOR.JSON ./main.py  
# ./main.py -f wor.json
# ./main.py -a world=мира

# Задание 1 Перевести программу на библеатеку argparse
# Задание 2 Добавить в программу аргумент -a который выведит принт 
# Задание 3 Добавить в программу аргумент -a который добавит слово в файл словаря

# сделать копию json!!!!