# Функции для создания и размещения поля на экране

import pygame

# Цвета
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

beige = (253,246,227)   		# Бежевый
light_brown = (201,153,126)		# Светло коричневый
#light_yellow = (255,255,98)
#light_green = (174,248,143)
light_yellow = (186,202,68)
light_green = (246, 246, 130)



def fff():
	print(5)


# Определяем будущую ширину и высоту экрана с игрой
def screen_resolution(additional_space = [0, 0],	# Дополнительное простроанство
					  amount_cell_x = 0,			# Количество клеток по горизонтали
					  amount_cell_y = 0,			# Количество клеток во вертикали
					  cell_width = 0,				# Толщина клеток
					  margin_width = 0):			# Тольщина границ между клетками

	FIELD_WIDTH = amount_cell_x * cell_width + (amount_cell_x + 1) * margin_width + additional_space[0]
	FIELD_HEIGHT = amount_cell_y * cell_width + (amount_cell_y + 1) * margin_width + additional_space[1]
	return FIELD_WIDTH, FIELD_HEIGHT



# >>>---------------------------- Функция создания поля ----------------------------<<<
def create_field(function,
				screen,		            # Экран
				field_array,			# Массив клеток
				amount_cell_x = 10,		# Количество клеток по горизонтали
				amount_cell_y = 10,		# Количество клеток во вертикали
				cell_width = 30,		# Толщина клеток
				margin_width = 1,		# Тольщина границ между клетками
				initial_spot = [0, 0],	# Место поля на экране
				color1 = light_brown,	# Цвет клеток
				color2 = None,			# Второй цвет клеток
				color_margin = black):	# Цвет границ


	# Находим ширину и высоту всего поля
	FIELD_WIDTH = amount_cell_x * cell_width + 2 * margin_width - 1
	FIELD_HEIGHT = amount_cell_y * cell_width + 2 * margin_width - 1

	
	# -------------- Рисуем границы (если надо) -------------- 
	if margin_width > 0:

		amount_margin_x = 2		# Количество вертикальных границ 
		amount_margin_y = 2		# Количество горизонтальных границ

		# Не понятно почему границы получались съехавшими и надо было поправлять точки границ.
		# Я так и не понял в чем тут дело, из-за чего они кривые, но способ исправить нашел..
		# Далается это при помощи вычитания у некоторых координат половины толщины границ и еще -1.
		# Вот толщину этих границ я и присваиваю этой переменной:
		extra_space = (margin_width/2) - 1


		# Рисуем вертикальные линии
		for i in range(amount_margin_x):

			if i == 0:
				point1 = (initial_spot[0], initial_spot[1] - extra_space)	 		# Координаты первой точки
				point2 = (initial_spot[0], FIELD_HEIGHT + initial_spot[1] - extra_space)	# Координаты второй точки
			else:
				point1 = (cell_width * amount_cell_x + margin_width  + initial_spot[0], initial_spot[1] - extra_space)	 		# Координаты первой точки
				point2 = (cell_width * amount_cell_x + margin_width  + initial_spot[0], FIELD_HEIGHT + initial_spot[1] - extra_space)	# Координаты второй точки

			pygame.draw.line(screen, color_margin, point1, point2, margin_width)


		# Рисуем горизонтальные линии
		for i in range(amount_margin_y):

			if i == 0:
				point1 = (initial_spot[0] - extra_space, initial_spot[1]) 			# Координаты первой точки
				point2 = (FIELD_WIDTH + initial_spot[0] - extra_space, initial_spot[1])	# Координаты второй точки
			else:
				point1 = (initial_spot[0] - extra_space, cell_width * amount_cell_y + margin_width + initial_spot[1]) 			# Координаты первой точки
				point2 = (FIELD_WIDTH + initial_spot[0] - extra_space, cell_width * amount_cell_y + margin_width + initial_spot[1])	# Координаты второй точки

			pygame.draw.line(screen, color_margin, point1, point2, margin_width)			


	# ----------------------------- Рисуем клетки -----------------------------
	for row in range(amount_cell_x):
		for column in range(amount_cell_y):

			# Если все клетки одного цвета
			if color2 == None:

				# Первоночально выглядящая клетка
				if field_array[row][column] == 0:
					x = cell_width * row + margin_width + initial_spot[0]
					y = cell_width * column + margin_width + initial_spot[1]
					pygame.draw.rect(screen, color1, (x, y, cell_width, cell_width))

				# Клетка отдается другой функции на изменение
				else:
					function()

			# Если клетки разных цветов
			else:

				x = cell_width * row + margin_width/2+1 + initial_spot[0]
				y = cell_width * column + margin_width/2+1 + initial_spot[1]

				# Первоночально выглядящие клетки
				if field_array[row][column] == 0:

					if (row + column) % 2 == 1:		# Если клетка нечетная
						pygame.draw.rect(screen, color1, (x, y, cell_width, cell_width))
					else:							# Если клетка четная
						pygame.draw.rect(screen, color2, (x, y, cell_width, cell_width))


				# Клетка отдается другой функции на изменение
				else:
					
					if (row + column) % 2 == 0:
						pygame.draw.rect(screen, light_green, (x, y, cell_width, cell_width))
					else:
						pygame.draw.rect(screen, light_yellow, (x, y, cell_width, cell_width))