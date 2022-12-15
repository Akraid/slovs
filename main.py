#!/usr/bin/python3

words = {
"introduction" : "вступление",
"secure" : "безопасный",
"oldest" : "старейший",
"net" : "сеть",
"network" : "сеть",
"networking" : "сетевое взаимодействие",
"encrypted" : "зашиврованное",
"encrypt" : "шифровать",
"communication" : "связь",
"between" : "между",
"remotely" : "удаленно",
"manage" : "управлять",
"service" : "сервис",
"server" : "сервер",
"other" : "другое",
"since" : "спустя",
"assets" : "активы",
"significant" : "значительно",
"granting" : "выдавать",
"access" : "доступ",
"сloud" : "облако",
"computing" : "вычисления",
"important" : "важный",
"even" : "даже",
"lets go" : "погнали",
"explore" : "изучать",
"shell" : "оболочка",
"develop" : "разрабатывать",
"developed" : "разработан",
"search" : "поиск",
"researcher" : "исследователь",
"sniffing" : "просеивание",
"thousands" : "тысячи",
"сredentials" : "секреты",
"which" : "который",
"want" : "хотеть",
"first" : "первый",
"revised" : "пересмотренный",
"to name" : "называть",
"force" : "сила",
"task force" : "рабочая сила",
"as" : "как",
"meahwhile" : "тем временем",
"sources" : "исходный код",
"eventually" : "в конечном итоге",
"led" : "привело",
"creation" : "создание",
"implementation" : "реализация",
"existance" : "существование",
"most" : "самый",
"etc" : "и так далее",
"through" : "через",
"another" : "другой",
"try" : "пытаться",
"call" : "вызов",
"called" : "называется",
"to access" : "получить доступ",
"probably" : "возможно",
"both" : "оба",
"should" : "должен",
"send" : "отправить",
"receive" : "получить",
"each other" : "друг от друга",
"fresh" : "свежий",
"refresh" : "обновить",
"done" : "сделано",
"same" : "тот же самый",
"in case of" : "в случае",
"public" : "публичный",
"only" : "только"
}

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

