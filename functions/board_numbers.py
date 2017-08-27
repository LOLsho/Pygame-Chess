# Номера и буковки по бокам доски

import pygame

def board_numbers(screen,
				  initial_spot = [0, 0],
				  cell_width = 80,
				  color = (143,96,80)):

	text_size = 25
	text_color = color

	numbers = ["8","7","6","5","4","3","2","1"]
	letters = ["a","b","c","d","e","f","g","h"]

	# Текст и его размер
	text_font = pygame.font.SysFont(("comicsansms"), text_size)


	for i in range(8):

		# Находим центр текста и совмещаем его с центром прямоугольника
		text_surf = text_font.render(numbers[i], True, text_color)
		text_rect = text_surf.get_rect()
		text_rect.center = (initial_spot[0] - 17, initial_spot[1] + (cell_width/2) + cell_width * i)

		# Выводим на экран
		screen.blit(text_surf, text_rect)


	for i in range(8):

		# Находим центр текста и совмещаем его с центром прямоугольника
		text_surf = text_font.render(letters[i], True, text_color)
		text_rect = text_surf.get_rect()
		text_rect.center = (initial_spot[0] + (cell_width/2) + cell_width * i, initial_spot[1] + cell_width * 8 + 17)

		# Выводим на экран
		screen.blit(text_surf, text_rect)