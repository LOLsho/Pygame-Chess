# Game Chess
# Written by Rukol Matvey
# 03.07.2017


# ------------------------- Импорты -------------------------
import sys                   # Импорт путей для модулей
sys.path.append("functions") # Путь к модулям с функциями

import pygame
from create_field import *
from main_meny import *
from buttons import *
from board_numbers import *
from manage_chessmen import *
from create_all_chassmen import *
#----------------------------------------------


# Выход из игры
def exit_game():
	pygame.quit()
	quit()


# ---------- Цвета ----------
black = (0,0,0)
beige = (232,214,194)   		# Бежевый
light_brown = (255,203,153)		# Светло коричневый
brown = (143,96,80)				# Коричневый для шахмат

# Сет цветов с сойта, в зеленом стиле
almost_white = (238,238,210)
green = (118, 150, 86)
#----------------------------



#------- Запускаем и настраиваем pygame -------
pygame.init()

# Звуки
pygame.mixer.music.load("sounds/Dreamy-ambient.mp3")
step_sound = pygame.mixer.Sound("sounds/step.wav")

WIN_WIDTH, WIN_HIGHT = screen_resolution(additional_space = [250, 50], amount_cell_x = 8, amount_cell_y = 8, cell_width = 80, margin_width = 0)

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HIGHT))

# Назначаем название приложения
pygame.display.set_caption("Chess")

# Иконка
icon_img = pygame.image.load("images/icon.jpg")
pygame.display.set_icon(icon_img)

clock = pygame.time.Clock()
#----------------------------------------------



#------------ Вводим параметры для игрового поля ------------

amount_cell_x = 8		# Количество клеток по горизонтали
amount_cell_y = 8		# Количество клеток во вертикали
cell_width = 80			# Толщина клеток
margin_width = 1		# Тольщина границ между клетками
color1 = green 			# Цвет клеток
color2 = almost_white	# Второй цвет клеток
color_margin = green	# Цвет границ

# Создаем матрицу клеток
field_array = [[0] * amount_cell_y for j in range(amount_cell_x)]

# Находим ширину и высоту всего поля
FIELD_WIDTH = amount_cell_x * cell_width + (amount_cell_x + 1) * margin_width
FIELD_HEIGHT = amount_cell_y * cell_width + (amount_cell_y + 1) * margin_width

# Место поля на экране
initial_spot = [30, 13]
#------------------------------------------------------------



# ---------------- Загружаем изображения фигур ----------------
img_white_pawn = pygame.image.load("images/chessmen/white_pawn.png")
img_white_rook = pygame.image.load("images/chessmen/white_rook.png")
img_white_knight = pygame.image.load("images/chessmen/white_knight.png")
img_white_bishop = pygame.image.load("images/chessmen/white_bishop.png")
img_white_queen = pygame.image.load("images/chessmen/white_queen.png")
img_white_king = pygame.image.load("images/chessmen/white_king.png")

img_black_pawn = pygame.image.load("images/chessmen/black_pawn.png")
img_black_rook = pygame.image.load("images/chessmen/black_rook.png")
img_black_knight = pygame.image.load("images/chessmen/black_knight.png")
img_black_bishop = pygame.image.load("images/chessmen/black_bishop.png")
img_black_queen = pygame.image.load("images/chessmen/black_queen.png")
img_black_king = pygame.image.load("images/chessmen/black_king.png")

imgs = [img_white_pawn, img_white_rook, img_white_knight, img_white_bishop, img_white_queen, img_white_king,
		img_black_pawn, img_black_rook, img_black_knight, img_black_bishop, img_black_queen, img_black_king]
#--------------------------------------------------------------




def game_loop():

	# Запускаем фоновою музыку
	music = "ON"
	pygame.mixer.music.play(-1)

	# Создаем матрицу клеток
	field_array = [[0] * amount_cell_y for j in range(amount_cell_x)]

	# Переменная для управления экранами в игре
	control = "main_meny"

	# Переменная для определения чей сейчас ход
	step = "white"

	# Переменная для взятия на проходе
	take_on_the_aisle = False

	# Переменная для рокировки
	castling = ["Not done","Not done"]

	# Есть ли сейчас активная клетка
	active_cell = None

	# Доступные ходы
	available_moves = []

	# Записываем предыдущие ходы
	turn_off = []

	# Создаем все фигуры
	all_chassmen = create_all_chassmen()

	# Пешка, дошедшая до конца
	brave_pawn = None

	# Король под атакой
	attacked = None


	# Цикл игры
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()


		# Меняем экран игры в зависимости от действий игрока

		if control == "main_meny":
			control = main_meny(screen)


		if control == "settings_meny":
			gg = settings_meny(screen, music)

			control = gg[0]
			music = gg[1]


		elif control == "gaming":  # Запускаем экран игры

			screen.fill(almost_white)

			create_field(fff, screen, field_array, amount_cell_x, amount_cell_y, cell_width, margin_width, initial_spot, color1, color2, color_margin)
			board_numbers(screen, initial_spot, cell_width, green)
		
			# ---------- Управление шахматными фигурами ----------
			gg = manage_chessmen(screen, initial_spot, all_chassmen, imgs, step, field_array, active_cell, available_moves, turn_off, castling, take_on_the_aisle, brave_pawn, attacked, step_sound)
				
			field_array = gg[0]
			active_cell = gg[1]
			available_moves = gg[2]
			all_chassmen = gg[3]
			step = gg[4]
			turn_off = gg[5]
			castling = gg[6]
			take_on_the_aisle = gg[7]
			brave_pawn = gg[8]
			attacked = gg[9]
			#------------------------------------------------------

			# Кнопка настроек
			gg = settings(screen, x = WIN_WIDTH-100, y=15, width = 70, height = 70, margin_width=2, img="images/pos2.png")

			pressed = gg

			if pressed == True:
				control = "settings_meny"


		elif control == "Exit":    # Выход из игры
			exit_game()


		# Выводим все на дисплей
		pygame.display.update()
		if attacked != None:
			time.sleep(1)
			attacked = None


		clock.tick(60)

game_loop()