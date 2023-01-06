#!/usr/bin/python3

import sys, json, os.path, random, shutil, os, slovs

cli = slovs.CommandLineInterface()

if len(sys.argv) > 1:
	match sys.argv[1]:
		case '-f':
			cli.file(sys.argv[2])
		case '-u':
			cli.update()
		case '-r':
			cli.reset()
		case '-l':
			cli.list()
		case '-d':
			cli.delete()
		case _:
			cli.error()

cli.check()

game = slovs.Gamewords(cli.getfilename())
game.print_vibor()

vibor = int(input())

match vibor:
	case 1:
			game.randommod()
	case 2:
			game.linemode()
	case _:
		print('Нужно выбрать 1 или 2')
print('Обновите очки в словаре')
