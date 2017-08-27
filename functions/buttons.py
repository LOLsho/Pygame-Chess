# Функция кнопки

import pygame
import colors
import time


def reward_for_brave_pawl(screen,
				  x = 0,
				  y = 0,
				  width = 100,
				  height = 50,
				  margin_width = 1,
				  color = (0,180,0),
				  color2 = (0,220,0),
				  color_margin = (0,0,0),
				  text = None,
				  text_size = 15,
				  text_color = (0,0,0),
				  img = None):

	# Переменные с позицией и кликами мыши
	mouse = pygame.mouse.get_pos() 
	click = pygame.mouse.get_pressed()
	

	# Рисуем границы если надо
	if margin_width > 0:
		
		pygame.draw.rect(screen, color_margin, (x - margin_width, y - margin_width, width + 2 * margin_width, height + 2 * margin_width))


	# Рисуем прямоугольник 
	pygame.draw.rect(screen, color, (x, y, width, height))


	# Если наводят и\или нажимают мышкой на кнопку 
	if x + width > mouse[0] > x and y + height > mouse[1] > y:
		pygame.draw.rect(screen, color2, (x, y, width, height)) 
		if click[0] == 1:
			return 1



	# Если кнопка - это загруженное изображение. Загружаем и выводим на экран.
	if img != None:
		button_img = pygame.image.load(img)

		img_rect = button_img.get_rect()
		img_rect.center = ((margin_width + 80)/ 2 + x, (margin_width + 80)/ 2 + y)

		screen.blit(button_img, img_rect)


	# Если есть текст
	if text != None:
		# Текст и его размер
		text_font = pygame.font.SysFont(("comicsansms"), text_size)

		# Находим центр текста и совмещаем его с центром прямоугольника
		text_surf = text_font.render(text, True, text_color)
		text_rect = text_surf.get_rect()
		text_rect.center = (x + (width/2), y + (height/2))

		# Выводим на экран
		screen.blit(text_surf, text_rect)

def meny_button(screen,
				x = 0,
				y = 0,
				width = 100,
				height = 50,
				margin_width = 1,
				color = (0,180,0),
				color2 = (0,220,0),
				color_margin = (0,0,0),
				text = None,
				text_size = 15,
				text_color = (0,0,0)):


	# Переменные с позицией и кликами мыши
	mouse = pygame.mouse.get_pos() 
	click = pygame.mouse.get_pressed()
	

	# Нажата ли кнопка
	pressed = False


	# Рисуем границы если надо
	if margin_width > 0:
		
		pygame.draw.rect(screen, color_margin, (x - margin_width, y - margin_width, width + 2 * margin_width, height + 2 * margin_width))



	# Рисуем прямоугольник 
	pygame.draw.rect(screen, color, (x, y, width, height))



	# Если наводят и\или нажимают мышкой на кнопку 
	if x + width > mouse[0] > x and y + height > mouse[1] > y:

		pygame.draw.rect(screen, color2, (x, y, width, height)) 

		if click[0] == 1:
			pressed = True
			time.sleep(0.2)




	# Если есть текст
	if text != None:
		# Текст и его размер
		text_font = pygame.font.SysFont(("comicsansms"), text_size)

		# Находим центр текста и совмещаем его с центром прямоугольника
		text_surf = text_font.render(text, True, text_color)
		text_rect = text_surf.get_rect()
		text_rect.center = (x + (width/2), y + (height/2))

		# Выводим на экран
		screen.blit(text_surf, text_rect)

	if pressed:
		return 1




def settings(screen,
				x = 0,
				y = 0,
				width = 70,
				height = 70,
				margin_width = 1,
				color = (0,180,0),
				color2 = (0,220,0),
				color_margin = (0,0,0),
				img = None):

	# Переменные с позицией и кликами мыши
	mouse = pygame.mouse.get_pos() 
	click = pygame.mouse.get_pressed()


	# Нажата ли кнопка
	pressed = False


	width = 70
	height = 70

	# Если наводят и\или нажимают мышкой на кнопку 
	if x + width > mouse[0] > x and y + height > mouse[1] > y:

		pygame.draw.rect(screen, colors.green, (x+4, y+2, width-8, height-4))
		pygame.draw.rect(screen, (0,0,0), (x+4, y+2, width-8, height-4), 1)

		if click[0] == 1:
			pressed = True


	# Если кнопка - это загруженное изображение. Загружаем и выводим на экран.
	if img != None:
		button_img = pygame.image.load(img)

		img_rect = button_img.get_rect()
		img_rect.center = (width / 2 + x, height / 2 + y)

		screen.blit(button_img, img_rect)


	return pressed