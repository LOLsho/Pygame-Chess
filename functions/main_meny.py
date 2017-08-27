# Главное меню игры

import pygame
import colors
import buttons



def main_meny(screen):

	img = pygame.image.load("images/background/chess-pawns2.jpg")

	# Buttons
	x = 150
	y = 100
	width = 200
	height = 35
	margin_width = 1
	color = colors.meny_background
	color2 = (228,228,222)
	color_margin = 1
	text_size = 20
	text_color = (0,0,0)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		# Выводим фоновую картинку
		screen.blit(img, [0,0])

		button1 = buttons.meny_button(screen, x, y+50, width, height, margin_width, color, color2, color_margin, "Play", text_size, text_color)
		button2 = buttons.meny_button(screen, x, y+100, width, height, margin_width, color, color2, color_margin, "Settings", text_size, text_color)
		button3 = buttons.meny_button(screen, x, y+150, width, height, margin_width, color, color2, color_margin, "Quit", text_size, text_color)



		pygame.display.update()

		if button1 != None:
			return "gaming"

		elif button2 != None:
			return "settings_meny"

		elif button3 != None:
			return "Exit"

def settings_meny(screen, music):

	img = pygame.image.load("images/background/chess-pawns2.jpg")

	# Buttons
	x = 150
	y = 100
	width = 200
	height = 35
	margin_width = 1
	color = colors.meny_background
	color2 = (228,228,222)
	color_margin = 1
	text_size = 20
	text_color = (0,0,0)


	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		# Выводим фоновую картинку
		screen.blit(img, [0,0])

		if music == "ON":
			button1 = buttons.meny_button(screen, x, y+50, width, height, margin_width, color, color2, color_margin, "Music: ON", text_size, text_color)
		else:
			button1 = buttons.meny_button(screen, x, y+50, width, height, margin_width, color, color2, color_margin, "Music: OFF", text_size, text_color)

		button3 = buttons.meny_button(screen, x, y+100, width, height, margin_width, color, color2, color_margin, "Back", text_size, text_color)



		pygame.display.update()

		if button1 != None:
			if music == "ON":
				pygame.mixer.music.stop()
				music = "OFF"
			else:
				music = "ON"
				pygame.mixer.music.play(-1)


		elif button3 != None:
			return ("main_meny", music)
