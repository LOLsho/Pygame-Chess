# Функция управления фигурами на поле

import pygame
from buttons import *
import colors
import time



def king_is_attacked(screen, initial_spot, cor_white_king, cor_black_king, step):

	img = pygame.image.load("images/r2r.png")

	if step == "white":
		x = cor_white_king[0] * 80 + 1 + initial_spot[0]
		y = cor_white_king[1] * 80 + 1 + initial_spot[1]

		screen.blit(img, [x,y])

	elif step == "black":
		x = cor_black_king[0] * 80 + 1 + initial_spot[0]
		y = cor_black_king[1] * 80 + 1 + initial_spot[1]

		screen.blit(img, [x,y])



def choose_something(screen, initial_spot, step, imgs):

		#pygame.draw.rect(screen, (0,0,0), (initial_spot[0]+201, initial_spot[1]+201, 240, 240))
		#draw_button(screen, initial_spot[0], initial_spot[1], )

		first_button = [initial_spot[0] + 238, initial_spot[1] + 240]

		# ------------------ Рисуем фон -------------------
		img = pygame.image.load("images/fon8811.png")
		img_rect = img.get_rect()
		img_rect.center = (4*80 + 1 + 27, 4*80 + 1 + 10)
		screen.blit(img, img_rect)
		#--------------------------------------------------


		# ----- Рисуем квадратики -----
		# Тут немного странно сдалал, но тут считай "если ход белых"
		if step != "white":

			manage = reward_for_brave_pawl(screen, x = first_button[0], y = first_button[1], width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/white_queen.png")
			if manage != None:
				return "white_queen"

			manage = reward_for_brave_pawl(screen, x = first_button[0] + 85, y = first_button[1], width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/white_rook.png")
			if manage != None:
				return "white_rook"

			manage = reward_for_brave_pawl(screen, x = first_button[0], y = first_button[1] + 85, width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/white_knight.png")
			if manage != None:
				return "white_knight"

			manage = reward_for_brave_pawl(screen, x = first_button[0] + 85, y = first_button[1] + 85, width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/white_bishop.png")
			if manage != None:
				return "white_bishop"

		# Если награду за пешку получают черные
		else:

			manage = reward_for_brave_pawl(screen, x = first_button[0], y = first_button[1], width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/black_queen.png")
			if manage != None:
				return "black_queen"

			manage = reward_for_brave_pawl(screen, x = first_button[0] + 85, y = first_button[1], width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/black_rook.png")
			if manage != None:
				return "black_rook"

			manage = reward_for_brave_pawl(screen, x = first_button[0], y = first_button[1] + 85, width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/black_knight.png")
			if manage != None:
				return "black_knight"

			manage = reward_for_brave_pawl(screen, x = first_button[0] + 85, y = first_button[1] + 85, width = 80, height = 80, margin_width = 1, color = colors.green, color2 = colors.almost_white, color_margin = (0,0,0), text = None, text_size = 15, text_color = (0,0,0), img = "images/chessmen/black_bishop.png")
			if manage != None:
				return "black_bishop"
    




def manage_chessmen(screen, initial_spot, all_chassmen, imgs, step, field_array, active_cell, available_moves, turn_off, castling, take_on_the_aisle, brave_pawn, attacked, step_sound):

	# imgs:

	# [0] - white_pawn       [6] - black_pawn
	# [1] - white_rook		 [7] - black_rook
	# [2] - white_knight	 [8] - black_knight
	# [3] - white_bishop	 [9] - black_bishop
	# [4] - white_queen		 [10] - black_queen
	# [5] - white_king 		 [11] - black_king


	# Переменные с позицией и кликами мыши
	mouse = pygame.mouse.get_pos() 
	click = pygame.mouse.get_pressed()


	# Цвета
	cell_width = 80 	# Толщина клетки
	#light_yellow = (255,255,98)
	#light_green = (174,248,143)

	# Сет цветов с сайта, в зеленом стиле
	light_yellow = (186,202,68)
	light_green = (246, 246, 130)

	attacked = None


	for x in range(8):
		for y in range(8):

			# Текущие координатиы мыши
			x_pos = initial_spot[0]+1 + (x * 80)  # Координата Х для каждой клетки
			y_pos = initial_spot[1]+1 + (y * 80)  # Координата Y для каждой клетки

			# Текущие координаты клетки, над которой находится мышь 
			if x_pos + cell_width > mouse[0] > x_pos and y_pos + cell_width > mouse[1] > y_pos:
				#pygame.draw.rect(screen, (0,0,0), (x_pos, y_pos, cell_width, cell_width)) 

				# Если нажали левой кнопкой мыши
				if click[0] == 1:

					# Если нету пешки, дошедшей до конца, то играем как играли)..
					if brave_pawn == None:
						# Если нету активной клетки
						if active_cell == None:
							if all_chassmen[x][y] != None:
								if all_chassmen[x][y][:5] == step:
									
									# Записываем клеточки для дальнейшей их деактивации и возвращения к стандартному цвету
									turn_off.append([x,y])

									# Меняем цвет активной клетки
									field_array[x][y] = 1

									# Записываем координаты активной клетки и фигуру, которая на ней стоит
									active_cell = [x, y, all_chassmen[x][y]]
									
									
						# Активная клетка есть, вычисляем ДОСТУПНЫЕ ХОДЫ
						else:
							# Если список доступных ходов еще пуст
							if available_moves == []:


								# ----------------------------->> БЕЛАЯ ПЕШКА <<-----------------------------
								if all_chassmen[active_cell[0]][active_cell[1]] == "white_pawn":

									# Просто ход на одну клетку вперед
									if all_chassmen[active_cell[0]][active_cell[1]-1] == None:
										available_moves.append([active_cell[0], active_cell[1]-1])
											
										# Ход на две клетки вперед
										if all_chassmen[active_cell[0]][active_cell[1]-2] == None and active_cell[1] == 6:
											available_moves.append([active_cell[0], active_cell[1]-2])


									# Скушать
									if active_cell[0] != 0 and active_cell[0] != 7:

										if all_chassmen[active_cell[0]-1][active_cell[1]-1] != None and all_chassmen[active_cell[0]-1][active_cell[1]-1][:5] != step:
											available_moves.append([active_cell[0]-1, active_cell[1]-1])

										if all_chassmen[active_cell[0]+1][active_cell[1]-1] != None and all_chassmen[active_cell[0]+1][active_cell[1]-1][:5] != step:
											available_moves.append([active_cell[0]+1, active_cell[1]-1])

									else:
										if active_cell[0] == 0:
											if all_chassmen[active_cell[0]+1][active_cell[1]-1] != None and all_chassmen[active_cell[0]+1][active_cell[1]-1][:5] != step:
												available_moves.append([active_cell[0]+1, active_cell[1]-1])
										else:
											if all_chassmen[active_cell[0]-1][active_cell[1]-1] != None and all_chassmen[active_cell[0]-1][active_cell[1]-1][:5] != step:
												available_moves.append([active_cell[0]-1, active_cell[1]-1])

									# Взятие на проходе
									if active_cell[1] == 3:

										if active_cell[0] != 0 and active_cell[0] != 7:

											# Вправо
											if turn_off[1][0] == active_cell[0] + 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 1:

												if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "black_pawn":
													available_moves.append([active_cell[0] + 1, active_cell[1] - 1])
													take_on_the_aisle = True

											# Влево
											if turn_off[1][0] == active_cell[0] - 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 1:

												if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "black_pawn":
													available_moves.append([active_cell[0] - 1, active_cell[1] - 1])
													take_on_the_aisle = True

										else:
											# Вправо
											if active_cell[0] == 0:
												if turn_off[1][0] == active_cell[0] + 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 1:
													if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "black_pawn":
														available_moves.append([active_cell[0] + 1, active_cell[1] - 1])
														take_on_the_aisle = True

											# Влево
											if active_cell[0] == 7:
												if turn_off[1][0] == active_cell[0] - 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 1:
													if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "black_pawn":
														available_moves.append([active_cell[0] - 1, active_cell[1] - 1])
														take_on_the_aisle = True

											

								# ----------------------------->> ЧЕРНАЯ ПЕШКА <<-----------------------------
								elif all_chassmen[active_cell[0]][active_cell[1]] == "black_pawn":

									# Просто ход
									if active_cell[1]+1 <= 7:
										if all_chassmen[active_cell[0]][active_cell[1]+1] == None:
											available_moves.append([active_cell[0], active_cell[1]+1])
												
											# Ход на две клетки вперед
											if active_cell[1] == 1:
												if all_chassmen[active_cell[0]][active_cell[1]+2] == None:
													available_moves.append([active_cell[0], active_cell[1]+2])

									# Скушать
									if active_cell[0] != 0 and active_cell[0] != 7:
										if active_cell[1]+1 <= 7:
											if all_chassmen[active_cell[0]+1][active_cell[1]+1] != None and all_chassmen[active_cell[0]+1][active_cell[1]+1][:5] != step:
												available_moves.append([active_cell[0]+1, active_cell[1]+1])

											if all_chassmen[active_cell[0]-1][active_cell[1]+1] != None and all_chassmen[active_cell[0]-1][active_cell[1]+1][:5] != step:
												available_moves.append([active_cell[0]-1, active_cell[1]+1])

									else:
										if active_cell[1]+1 <= 7:
											if active_cell[0] == 0:
												if all_chassmen[active_cell[0]+1][active_cell[1]+1] != None and all_chassmen[active_cell[0]+1][active_cell[1]+1][:5] != step:
													available_moves.append([active_cell[0]+1, active_cell[1]+1])
											else:
												if all_chassmen[active_cell[0]-1][active_cell[1]+1] != None and all_chassmen[active_cell[0]-1][active_cell[1]+1][:5] != step:
													available_moves.append([active_cell[0]-1, active_cell[1]+1])

									# Взятие на проходе
									if active_cell[1] == 4:

										if active_cell[0] != 0 and active_cell[0] != 7:

											# Вправо
											if turn_off[1][0] == active_cell[0] + 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 6:

												if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "white_pawn":
													available_moves.append([active_cell[0] + 1, active_cell[1] + 1])
													take_on_the_aisle = True

											# Влево
											if turn_off[1][0] == active_cell[0] - 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 6:
												print(take_on_the_aisle)
												if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "white_pawn":
													available_moves.append([active_cell[0] - 1, active_cell[1] + 1])
													take_on_the_aisle = True

										else:
											# Вправо
											if active_cell[0] == 0:
												if turn_off[1][0] == active_cell[0] + 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 6:
													if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "white_pawn":
														available_moves.append([active_cell[0] + 1, active_cell[1] + 1])
														take_on_the_aisle = True
											# Влево
											if active_cell[0] == 7:
												if turn_off[1][0] == active_cell[0] - 1 and turn_off[1][1] == active_cell[1] and turn_off[0][1] == 6:
													if all_chassmen[turn_off[1][0]][turn_off[1][1]] == "white_pawn":
														available_moves.append([active_cell[0] - 1, active_cell[1] + 1])
														take_on_the_aisle = True



								# -------------------------------->> ЛАДЬЯ <<--------------------------------
								elif all_chassmen[active_cell[0]][active_cell[1]] == "white_rook" or all_chassmen[active_cell[0]][active_cell[1]] == "black_rook":
									move = 1


									# Ходы по одному ВВЕРХ
									if 7 >= active_cell[1] - move >= 0:
										while all_chassmen[active_cell[0]][active_cell[1]-move] == None:
											available_moves.append([active_cell[0], active_cell[1]-move])
											move += 1

											if active_cell[1] - move < 0:
												break


										# Съедает
										else:
											if 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0], active_cell[1]-move])
									move = 1


									# Ходы по одному ВНИЗ
									if 7 >= active_cell[1] + move >= 0:
										while all_chassmen[active_cell[0]][active_cell[1]+move] == None:
											available_moves.append([active_cell[0], active_cell[1]+move])
											move += 1

											if active_cell[1] + move > 7:
												break

										# Съедает
										else:
											if 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0], active_cell[1]+move])
									move = 1


									# Ходы по одному ВЛЕВО
									if 7 >= active_cell[0] - move >= 0:
										while all_chassmen[active_cell[0]-move][active_cell[1]] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]])
											move += 1

											if active_cell[0] - move < 0:
												break

										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]])
									move = 1


									# Ходы по одному ВПРАВО
									if 7 >= active_cell[0] + move >= 0:
										while all_chassmen[active_cell[0]+move][active_cell[1]] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]])
											move += 1

											if active_cell[0] + move > 7:
												break

										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]])



								# -------------------------------->> СЛОН <<--------------------------------
								elif all_chassmen[active_cell[0]][active_cell[1]] == "white_bishop" or all_chassmen[active_cell[0]][active_cell[1]] == "black_bishop":
									move = 1
									

									# Ходы по одному ВВЕРХ-ВЛЕВО
									if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] - move >= 0:
										while all_chassmen[active_cell[0]-move][active_cell[1]-move] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]-move])
											move += 1

											if active_cell[0] - move < 0 or active_cell[1] - move < 0:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]-move])
									move = 1



									# Ходы по одному ВВЕРХ-ВПРАВО
									if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] - move >= 0:
										while all_chassmen[active_cell[0]+move][active_cell[1]-move] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]-move])
											move += 1

											if active_cell[0] + move > 7 or active_cell[1] - move < 0:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]-move])
									move = 1



									# Ходы по одному ВНИЗ-ВПРАВО
									if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] + move >= 0:
										while all_chassmen[active_cell[0]+move][active_cell[1]+move] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]+move])
											move += 1

											if active_cell[0] + move > 7 or active_cell[1] + move > 7:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]+move])
									move = 1



									# Ходы по одному ВНИЗ-ВЛЕВО
									if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] + move >= 0:
										while all_chassmen[active_cell[0]-move][active_cell[1]+move] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]+move])
											move += 1

											if active_cell[0] - move < 0 or active_cell[1] + move > 7:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]+move])



								# -------------------------------->> КОНЬ <<--------------------------------
								elif all_chassmen[active_cell[0]][active_cell[1]] == "white_knight" or all_chassmen[active_cell[0]][active_cell[1]] == "black_knight":
									long_move = 2
									short_move = 1

									# Ход ВВЕРХ-ВЛЕВО
									if 7 >= active_cell[0] - short_move >= 0 and 7 >= active_cell[1] - long_move >= 0:
										if all_chassmen[active_cell[0]-short_move][active_cell[1]-long_move] == None:
											available_moves.append([active_cell[0]-short_move, active_cell[1]-long_move])

										# Съедает
										else:
											if 7 >= active_cell[0] - short_move >= 0 and 7 >= active_cell[1] - long_move >= 0:
												if step != all_chassmen[active_cell[0]-short_move][active_cell[1]-long_move][:5]:
													available_moves.append([active_cell[0]-short_move, active_cell[1]-long_move])



									# Ход ВВЕРХ-ПРАВО
									if 7 >= active_cell[0] + short_move >= 0 and 7 >= active_cell[1] - long_move >= 0:
										if all_chassmen[active_cell[0]+short_move][active_cell[1]-long_move] == None:
											available_moves.append([active_cell[0]+short_move, active_cell[1]-long_move])

										# Съедает
										else:
											if 7 >= active_cell[0] + short_move >= 0 and 7 >= active_cell[1] - long_move >= 0:
												if step != all_chassmen[active_cell[0]+short_move][active_cell[1]-long_move][:5]:
													available_moves.append([active_cell[0]+short_move, active_cell[1]-long_move])


									# Ход ВПРАВО-ВВЕРХ
									if 7 >= active_cell[0] + long_move >= 0 and 7 >= active_cell[1] - short_move >= 0:
										if all_chassmen[active_cell[0]+long_move][active_cell[1]-short_move] == None:
											available_moves.append([active_cell[0]+long_move, active_cell[1]-short_move])

										# Съедает
										else:
											if 7 >= active_cell[0] + long_move >= 0 and 7 >= active_cell[1] - short_move >= 0:
												if step != all_chassmen[active_cell[0]+long_move][active_cell[1]-short_move][:5]:
													available_moves.append([active_cell[0]+long_move, active_cell[1]-short_move])


									# Ход ВПРАВО-ВНИЗ
									if 7 >= active_cell[0] + long_move >= 0 and 7 >= active_cell[1] + short_move >= 0:
										if all_chassmen[active_cell[0]+long_move][active_cell[1]+short_move] == None:
											available_moves.append([active_cell[0]+long_move, active_cell[1]+short_move])

										# Съедает
										else:
											if 7 >= active_cell[0] + long_move >= 0 and 7 >= active_cell[1] + short_move >= 0:
												if step != all_chassmen[active_cell[0]+long_move][active_cell[1]+short_move][:5]:
													available_moves.append([active_cell[0]+long_move, active_cell[1]+short_move])


									# Ход ВНИЗ-ВПРАВО
									if 7 >= active_cell[0] + short_move >= 0 and 7 >= active_cell[1] + long_move >= 0:
										if all_chassmen[active_cell[0]+short_move][active_cell[1]+long_move] == None:
											available_moves.append([active_cell[0]+short_move, active_cell[1]+long_move])

										# Съедает
										else:
											if 7 >= active_cell[0] + short_move >= 0 and 7 >= active_cell[1] + long_move >= 0:
												if step != all_chassmen[active_cell[0]+short_move][active_cell[1]+long_move][:5]:
													available_moves.append([active_cell[0]+short_move, active_cell[1]+long_move])


									# Ход ВНИЗ-ВЛЕВО
									if 7 >= active_cell[0] - short_move >= 0 and 7 >= active_cell[1] + long_move >= 0:
										if all_chassmen[active_cell[0]-short_move][active_cell[1]+long_move] == None:
											available_moves.append([active_cell[0]-short_move, active_cell[1]+long_move])

										# Съедает
										else:
											if 7 >= active_cell[0] - short_move >= 0 and 7 >= active_cell[1] + long_move >= 0:
												if step != all_chassmen[active_cell[0]-short_move][active_cell[1]+long_move][:5]:
													available_moves.append([active_cell[0]-short_move, active_cell[1]+long_move])


									# Ход ВЛЕВО-ВНИЗ
									if 7 >= active_cell[0] - long_move >= 0 and 7 >= active_cell[1] + short_move >= 0:
										if all_chassmen[active_cell[0]-long_move][active_cell[1]+short_move] == None:
											available_moves.append([active_cell[0]-long_move, active_cell[1]+short_move])

										# Съедает
										else:
											if 7 >= active_cell[0] - long_move >= 0 and 7 >= active_cell[1] + short_move >= 0:
												if step != all_chassmen[active_cell[0]-long_move][active_cell[1]+short_move][:5]:
													available_moves.append([active_cell[0]-long_move, active_cell[1]+short_move])


									# Ход ВЛЕВО-ВВЕРХ
									if 7 >= active_cell[0] - long_move >= 0 and 7 >= active_cell[1] - short_move >= 0:
										if all_chassmen[active_cell[0]-long_move][active_cell[1]-short_move] == None:
											available_moves.append([active_cell[0]-long_move, active_cell[1]-short_move])

										# Съедает
										else:
											if 7 >= active_cell[0] - long_move >= 0 and 7 >= active_cell[1] - short_move >= 0:
												if step != all_chassmen[active_cell[0]-long_move][active_cell[1]-short_move][:5]:
													available_moves.append([active_cell[0]-long_move, active_cell[1]-short_move])



								# -------------------------------->> ФЕРЗЬ <<--------------------------------
								elif all_chassmen[active_cell[0]][active_cell[1]] == "white_queen" or all_chassmen[active_cell[0]][active_cell[1]] == "black_queen":
									move = 1
									

									# Ходы по одному ВВЕРХ-ВЛЕВО
									if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] - move >= 0:
										while all_chassmen[active_cell[0]-move][active_cell[1]-move] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]-move])
											move += 1

											if active_cell[0] - move < 0 or active_cell[1] - move < 0:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]-move])
									move = 1



									# Ходы по одному ВВЕРХ-ВПРАВО
									if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] - move >= 0:
										while all_chassmen[active_cell[0]+move][active_cell[1]-move] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]-move])
											move += 1

											if active_cell[0] + move > 7 or active_cell[1] - move < 0:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]-move])
									move = 1



									# Ходы по одному ВНИЗ-ВПРАВО
									if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] + move >= 0:
										while all_chassmen[active_cell[0]+move][active_cell[1]+move] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]+move])
											move += 1

											if active_cell[0] + move > 7 or active_cell[1] + move > 7:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]+move])
									move = 1



									# Ходы по одному ВНИЗ-ВЛЕВО
									if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] + move >= 0:
										while all_chassmen[active_cell[0]-move][active_cell[1]+move] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]+move])
											move += 1

											if active_cell[0] - move < 0 or active_cell[1] + move > 7:
												break


										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]+move])
									move = 1



									# Ходы по одному ВВЕРХ
									if 7 >= active_cell[1] - move >= 0:
										while all_chassmen[active_cell[0]][active_cell[1]-move] == None:
											available_moves.append([active_cell[0], active_cell[1]-move])
											move += 1

											if active_cell[1] - move < 0:
												break


										# Съедает
										else:
											if 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0], active_cell[1]-move])
									move = 1


									# Ходы по одному ВНИЗ
									if 7 >= active_cell[1] + move >= 0:
										while all_chassmen[active_cell[0]][active_cell[1]+move] == None:
											available_moves.append([active_cell[0], active_cell[1]+move])
											move += 1

											if active_cell[1] + move > 7:
												break

										# Съедает
										else:
											if 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0], active_cell[1]+move])
									move = 1


									# Ходы по одному ВЛЕВО
									if 7 >= active_cell[0] - move >= 0:
										while all_chassmen[active_cell[0]-move][active_cell[1]] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]])
											move += 1

											if active_cell[0] - move < 0:
												break

										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]])
									move = 1


									# Ходы по одному ВПРАВО
									if 7 >= active_cell[0] + move >= 0:
										while all_chassmen[active_cell[0]+move][active_cell[1]] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]])
											move += 1

											if active_cell[0] + move > 7:
												break

										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]])



								# -------------------------------->> КОРОЛЬ <<--------------------------------
								elif all_chassmen[active_cell[0]][active_cell[1]] == "white_king" or all_chassmen[active_cell[0]][active_cell[1]] == "black_king":
									move = 1

									# Ход ВВЕРХ
									if 7 >= active_cell[0] >= 0 and 7 >= active_cell[1] - move >= 0:
										if all_chassmen[active_cell[0]][active_cell[1]-move] == None:
											available_moves.append([active_cell[0], active_cell[1]-move])

										# Съедает
										else:
											if 7 >= active_cell[0] >= 0 and 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0], active_cell[1]-move])


									# Ход ВНИЗ
									if 7 >= active_cell[0] >= 0 and 7 >= active_cell[1] + move >= 0:
										if all_chassmen[active_cell[0]][active_cell[1]+move] == None:
											available_moves.append([active_cell[0], active_cell[1]+move])

										# Съедает
										else:
											if 7 >= active_cell[0] >= 0 and 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0], active_cell[1]+move])


									# Ход ВЛЕВО
									if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] >= 0:
										if all_chassmen[active_cell[0]-move][active_cell[1]] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]])

										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]])


									# Ход ВПРАВО
									if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] >= 0:
										if all_chassmen[active_cell[0]+move][active_cell[1]] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]])

										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]])


									# Ход ВВЕРХ-ВЛЕВО
									if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] - move >= 0:
										if all_chassmen[active_cell[0]-move][active_cell[1]-move] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]-move])

										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]-move])


									# Ход ВВЕРХ-ВПРАВО
									if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] - move >= 0:
										if all_chassmen[active_cell[0]+move][active_cell[1]-move] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]-move])

										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] - move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]-move][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]-move])


									# Ход ВНИЗ-ВЛЕВО
									if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] + move >= 0:
										if all_chassmen[active_cell[0]-move][active_cell[1]+move] == None:
											available_moves.append([active_cell[0]-move, active_cell[1]+move])

										# Съедает
										else:
											if 7 >= active_cell[0] - move >= 0 and 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]-move][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0]-move, active_cell[1]+move])


									# Ход ВНИЗ-ВПРАВО
									if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] + move >= 0:
										if all_chassmen[active_cell[0]+move][active_cell[1]+move] == None:
											available_moves.append([active_cell[0]+move, active_cell[1]+move])

										# Съедает
										else:
											if 7 >= active_cell[0] + move >= 0 and 7 >= active_cell[1] + move >= 0:
												if step != all_chassmen[active_cell[0]+move][active_cell[1]+move][:5]:
													available_moves.append([active_cell[0]+move, active_cell[1]+move])


									# ----- РОКИРОВКА для БЕЛОГО короля -----
									if castling[0] == "Not done":
										if active_cell[2] == "white_king":
											# Проверка стоит ли король на подобающем для рокировки месте
											if [active_cell[0],active_cell[1]] == [4, 7]:

												# Проверка пустые ли клетки между королем и ладьей ВПРАВО
												if all_chassmen[active_cell[0] + 1][active_cell[1]] == None and all_chassmen[active_cell[0] + 2][active_cell[1]] == None:
													if all_chassmen[active_cell[0] + 3][active_cell[1]] == "white_rook":
														available_moves.append([active_cell[0]+2, active_cell[1]])


												# Проверка пустые ли клетки между королем и ладьей ВЛЕВО
												if all_chassmen[active_cell[0] - 1][active_cell[1]] == None and all_chassmen[active_cell[0] - 2][active_cell[1]] == None and all_chassmen[active_cell[0] - 3][active_cell[1]] == None:
													if all_chassmen[active_cell[0] - 4][active_cell[1]] == "white_rook":
														available_moves.append([active_cell[0]-2, active_cell[1]])


									# ----- РОКИРОВКА для ЧЕРНОГО короля -----
									if castling[1] == "Not done":
										if active_cell[2] == "black_king":
											# Проверка стоит ли король на подобающем для рокировки месте
											if [active_cell[0],active_cell[1]] == [4, 0]:

												# Проверка пустые ли клетки между королем и ладьей ВПРАВО
												if all_chassmen[active_cell[0] + 1][active_cell[1]] == None and all_chassmen[active_cell[0] + 2][active_cell[1]] == None:
													if all_chassmen[active_cell[0] + 3][active_cell[1]] == "black_rook":
														available_moves.append([active_cell[0]+2, active_cell[1]])


												# Проверка пустые ли клетки между королем и ладьей ВЛЕВО
												if all_chassmen[active_cell[0] - 1][active_cell[1]] == None and all_chassmen[active_cell[0] - 2][active_cell[1]] == None and all_chassmen[active_cell[0] - 3][active_cell[1]] == None:
													if all_chassmen[active_cell[0] - 4][active_cell[1]] == "black_rook":
														available_moves.append([active_cell[0]-2, active_cell[1]])



					# Вычисляем клетки под атакой
					# Если потом не влом будет убери if True
					if True:
						if [x,y] in available_moves:

							# Координаты клеток под атакой
							under_attack = []


							# Записываем где стояли фигуры на случай если после хода король стал под атакой
							chassman1 = all_chassmen[x][y]
							chassman2 = all_chassmen[active_cell[0]][active_cell[1]]

							# Перемещаем положение фигуры в списке фигур
							all_chassmen[x][y] = active_cell[2]
							all_chassmen[active_cell[0]][active_cell[1]] = None
							
							# Находим клетки под атакой
							for i in range(8):
								for j in range(8):
									if all_chassmen[i][j] != None:
										if all_chassmen[i][j][:5] != step:

											# ----- Клетки под атакой от БЕЛОЙ ПЕШКИ -----
											if all_chassmen[i][j] == "white_pawn":

												if i != 0 and i != 7:

													if all_chassmen[i-1][j-1] == None or all_chassmen[i-1][j-1][:5] == step:
														if [i-1, j-1] not in under_attack:
															under_attack.append([i-1, j-1])
													
													if all_chassmen[i+1][j-1] == None or all_chassmen[i+1][j-1][:5] == step:
														if [i+1, j-1] not in under_attack:
															under_attack.append([i+1, j-1])

												else:
													if i == 0:
														if all_chassmen[i+1][j-1] == None or all_chassmen[i+1][j-1][:5] == step:
															if [i+1, j-1] not in under_attack:
																under_attack.append([i+1, j-1])
													else:
														if all_chassmen[i-1][j-1] == None or all_chassmen[i-1][j-1][:5] == step:
															if [i-1, j-1] not in under_attack:
																under_attack.append([i-1, j-1])


											# ----- Клетки под атакой от ЧЕРНОЙ ПЕШКИ -----
											if all_chassmen[i][j] == "black_pawn":
												if i != 0 and i != 7:

													if all_chassmen[i-1][j+1] == None or all_chassmen[i-1][j+1][:5] == step:
														if [i-1, j+1] not in under_attack:
															under_attack.append([i-1, j+1])
													
													if all_chassmen[i+1][j+1] == None or all_chassmen[i+1][j+1][:5] == step:
														if [i+1, j+1] not in under_attack:
															under_attack.append([i+1, j+1])

												else:
													if i == 0:
														if all_chassmen[i+1][j+1] == None or all_chassmen[i+1][j+1][:5] == step:
															if [i+1, j+1] not in under_attack:
																under_attack.append([i+1, j+1])
													else:
														if all_chassmen[i-1][j+1] == None or all_chassmen[i-1][j+1][:5] == step:
															if [i-1, j+1] not in under_attack:
																under_attack.append([i-1, j+1])


											# -------------------------------->> ЛАДЬЯ <<--------------------------------
											elif all_chassmen[i][j] == "white_rook" or all_chassmen[i][j] == "black_rook":
												move = 1


												# Ходы по одному ВВЕРХ
												if 7 >= j - move >= 0:
													while all_chassmen[i][j-move] == None:
														if [i, j-move] not in under_attack:
															under_attack.append([i, j-move])
														move += 1

														if j - move < 0:
															break


													# Съедает
													else:
														if 7 >= j - move >= 0:
															if step == all_chassmen[i][j-move][:5]:
																if [i, j-move] not in under_attack:
																	under_attack.append([i, j-move])
												move = 1


												# Ходы по одному ВНИЗ
												if 7 >= j + move >= 0:
													while all_chassmen[i][j+move] == None:
														if [i, j+move] not in under_attack:
															under_attack.append([i, j+move])
														move += 1

														if j + move > 7:
															break


													# Съедает
													else:
														if 7 >= j + move >= 0:
															if step == all_chassmen[i][j+move][:5]:
																if [i, j+move] not in under_attack:
																	under_attack.append([i, j+move])
												move = 1


												# Ходы по одному ВЛЕВО
												if 7 >= i - move >= 0:
													while all_chassmen[i-move][j] == None:
														if [i-move, j] not in under_attack:
															under_attack.append([i-move, j])
														move += 1

														if i - move < 0:
															break

													# Съедает
													else:
														if 7 >= i - move >= 0:
															if step == all_chassmen[i-move][j][:5]:
																if [i-move, j] not in under_attack:
																	under_attack.append([i-move, j])
												move = 1


												# Ходы по одному ВПРАВО
												if 7 >= i + move >= 0:
													while all_chassmen[i+move][j] == None:
														if [i+move, j] not in under_attack:
															under_attack.append([i+move, j])
														move += 1

														if i + move > 7:
															break

													# Съедает
													else:
														if 7 >= i + move >= 0:
															if step == all_chassmen[i+move][j][:5]:
																if [i+move, j] not in under_attack:
																	under_attack.append([i+move, j])



											# -------------------------------->> СЛОН <<--------------------------------
											elif all_chassmen[i][j] == "white_bishop" or all_chassmen[i][j] == "black_bishop":
												move = 1
												

												# Ходы по одному ВВЕРХ-ВЛЕВО
												if 7 >= i - move >= 0 and 7 >= j - move >= 0:
													while all_chassmen[i-move][j-move] == None:
														if [i-move, j-move] not in under_attack:
															under_attack.append([i-move, j-move])
														move += 1

														if i - move < 0 or j - move < 0:
															break


													# Съедает
													else:
														if 7 >= i - move >= 0 and 7 >= j - move >= 0:
															if step == all_chassmen[i-move][j-move][:5]:
																if [i-move, j-move] not in under_attack:
																	under_attack.append([i-move, j-move])
												move = 1



												# Ходы по одному ВВЕРХ-ВПРАВО
												if 7 >= i + move >= 0 and 7 >= j - move >= 0:
													while all_chassmen[i+move][j-move] == None:
														if [i+move, j-move] not in under_attack:
															under_attack.append([i+move, j-move])
														move += 1

														if i + move > 7 or j - move < 0:
															break


													# Съедает
													else:
														if 7 >= i + move >= 0 and 7 >= j - move >= 0:
															if step == all_chassmen[i+move][j-move][:5]:
																if [i+move, j-move] not in under_attack:
																	under_attack.append([i+move, j-move])
												move = 1



												# Ходы по одному ВНИЗ-ВПРАВО
												if 7 >= i + move >= 0 and 7 >= j + move >= 0:
													while all_chassmen[i+move][j+move] == None:
														if [i+move, j+move] not in under_attack:
															under_attack.append([i+move, j+move])
														move += 1

														if i + move > 7 or j + move > 7:
															break


													# Съедает
													else:
														if 7 >= i + move >= 0 and 7 >= j + move >= 0:
															if step == all_chassmen[i+move][j+move][:5]:
																if [i+move, j+move] not in under_attack:
																	under_attack.append([i+move, j+move])
												move = 1



												# Ходы по одному ВНИЗ-ВЛЕВО
												if 7 >= i - move >= 0 and 7 >= j + move >= 0:
													while all_chassmen[i-move][j+move] == None:
														if [i-move, j+move] not in under_attack:
															under_attack.append([i-move, j+move])
														move += 1

														if i - move < 0 or j + move > 7:
															break


													# Съедает
													else:
														if 7 >= i - move >= 0 and 7 >= j + move >= 0:
															if step == all_chassmen[i-move][j+move][:5]:
																if [i-move, j+move] not in under_attack:
																	under_attack.append([i-move, j+move])



											# -------------------------------->> КОНЬ <<--------------------------------
											elif all_chassmen[i][j] == "white_knight" or all_chassmen[i][j] == "black_knight":
												long_move = 2
												short_move = 1

												# Ход ВВЕРХ-ВЛЕВО
												if 7 >= i - short_move >= 0 and 7 >= j - long_move >= 0:
													if all_chassmen[i-short_move][j-long_move] == None:
														if [i-short_move, j-long_move] not in under_attack:
															under_attack.append([i-short_move, j-long_move])

													# Съедает
													else:
														if 7 >= i - short_move >= 0 and 7 >= j - long_move >= 0:
															if step == all_chassmen[i-short_move][j-long_move][:5]:
																if [i-short_move, j-long_move] not in under_attack:
																	under_attack.append([i-short_move, j-long_move])



												# Ход ВВЕРХ-ВПРАВО
												if 7 >= i + short_move >= 0 and 7 >= j - long_move >= 0:
													if all_chassmen[i+short_move][j-long_move] == None:
														if [i+short_move, j-long_move] not in under_attack:
															under_attack.append([i+short_move, j-long_move])

													# Съедает
													else:
														if 7 >= i + short_move >= 0 and 7 >= j - long_move >= 0:
															if step == all_chassmen[i+short_move][j-long_move][:5]:
																if [i+short_move, j-long_move] not in under_attack:
																	under_attack.append([i+short_move, j-long_move])


												# Ход ВПРАВО-ВВЕРХ
												if 7 >= i + long_move >= 0 and 7 >= j - short_move >= 0:
													if all_chassmen[i+long_move][j-short_move] == None:
														if [i+long_move, j-short_move] not in under_attack:
															under_attack.append([i+long_move, j-short_move])

													# Съедает
													else:
														if 7 >= i + long_move >= 0 and 7 >= j - short_move >= 0:
															if step == all_chassmen[i+long_move][j-short_move][:5]:
																if [i+long_move, j-short_move] not in under_attack:
																	under_attack.append([i+long_move, j-short_move])


												# Ход ВПРАВО-ВНИЗ
												if 7 >= i + long_move >= 0 and 7 >= j + short_move >= 0:
													if all_chassmen[i+long_move][j+short_move] == None:
														if [i+long_move, j+short_move] not in under_attack:
															under_attack.append([i+long_move, j+short_move])

													# Съедает
													else:
														if 7 >= i + long_move >= 0 and 7 >= j + short_move >= 0:
															if step == all_chassmen[i+long_move][j+short_move][:5]:
																if [i+long_move, j+short_move] not in under_attack:
																	under_attack.append([i+long_move, j+short_move])


												# Ход ВНИЗ-ВПРАВО
												if 7 >= i + short_move >= 0 and 7 >= j + long_move >= 0:
													if all_chassmen[i+short_move][j+long_move] == None:
														if [i+short_move, j+long_move] not in under_attack:
															under_attack.append([i+short_move, j+long_move])

													# Съедает
													else:
														if 7 >= i + short_move >= 0 and 7 >= j + long_move >= 0:
															if step == all_chassmen[i+short_move][j+long_move][:5]:
																if [i+short_move, j+long_move] not in under_attack:
																	under_attack.append([i+short_move, j+long_move])


												# Ход ВНИЗ-ВЛЕВО
												if 7 >= i - short_move >= 0 and 7 >= j + long_move >= 0:
													if all_chassmen[i-short_move][j+long_move] == None:
														if [i-short_move, j+long_move] not in under_attack:
															under_attack.append([i-short_move, j+long_move])

													# Съедает
													else:
														if 7 >= i - short_move >= 0 and 7 >= j + long_move >= 0:
															if step == all_chassmen[i-short_move][j+long_move][:5]:
																if [i-short_move, j+long_move] not in under_attack:
																	under_attack.append([i-short_move, j+long_move])


												# Ход ВЛЕВО-ВНИЗ
												if 7 >= i - long_move >= 0 and 7 >= j + short_move >= 0:
													if all_chassmen[i-long_move][j+short_move] == None:
														if [i-long_move, j+short_move] not in under_attack:
															under_attack.append([i-long_move, j+short_move])

													# Съедает
													else:
														if 7 >= i - long_move >= 0 and 7 >= j + short_move >= 0:
															if step == all_chassmen[i-long_move][j+short_move][:5]:
																if [i-long_move, j+short_move] not in under_attack:
																	under_attack.append([i-long_move, j+short_move])


												# Ход ВЛЕВО-ВВЕРХ
												if 7 >= i - long_move >= 0 and 7 >= j - short_move >= 0:
													if all_chassmen[i-long_move][j-short_move] == None:
														if [i-long_move, j-short_move] not in under_attack:
															under_attack.append([i-long_move, j-short_move])

													# Съедает
													else:
														if 7 >= i - long_move >= 0 and 7 >= j - short_move >= 0:
															if step == all_chassmen[i-long_move][j-short_move][:5]:
																if [i-long_move, j-short_move] not in under_attack:
																	under_attack.append([i-long_move, j-short_move])



											# -------------------------------->> ФЕРЗЬ <<--------------------------------
											elif all_chassmen[i][j] == "white_queen" or all_chassmen[i][j] == "black_queen":
												move = 1
												

												# Ходы по одному ВВЕРХ-ВЛЕВО
												if 7 >= i - move >= 0 and 7 >= j - move >= 0:
													while all_chassmen[i-move][j-move] == None:
														if [i-move, j-move] not in under_attack:
															under_attack.append([i-move, j-move])
														move += 1

														if i - move < 0 or j - move < 0:
															break


													# Съедает
													else:
														if 7 >= i - move >= 0 and 7 >= j - move >= 0:
															if step == all_chassmen[i-move][j-move][:5]:
																if [i-move, j-move] not in under_attack:
																	under_attack.append([i-move, j-move])
												move = 1



												# Ходы по одному ВВЕРХ-ВПРАВО
												if 7 >= i + move >= 0 and 7 >= j - move >= 0:
													while all_chassmen[i+move][j-move] == None:
														if [i+move, j-move] not in under_attack:
															under_attack.append([i+move, j-move])
														move += 1

														if i + move > 7 or j - move < 0:
															break


													# Съедает
													else:
														if 7 >= i + move >= 0 and 7 >= j - move >= 0:
															if step == all_chassmen[i+move][j-move][:5]:
																if [i+move, j-move] not in under_attack:
																	under_attack.append([i+move, j-move])
												move = 1



												# Ходы по одному ВНИЗ-ВПРАВО
												if 7 >= i + move >= 0 and 7 >= j + move >= 0:
													while all_chassmen[i+move][j+move] == None:
														if [i+move, j+move] not in under_attack:
															under_attack.append([i+move, j+move])
														move += 1

														if i + move > 7 or j + move > 7:
															break


													# Съедает
													else:
														if 7 >= i + move >= 0 and 7 >= j + move >= 0:
															if step == all_chassmen[i+move][j+move][:5]:
																if [i+move, j+move] not in under_attack:
																	under_attack.append([i+move, j+move])
												move = 1



												# Ходы по одному ВНИЗ-ВЛЕВО
												if 7 >= i - move >= 0 and 7 >= j + move >= 0:
													while all_chassmen[i-move][j+move] == None:
														if [i-move, j+move] not in under_attack:
															under_attack.append([i-move, j+move])
														move += 1

														if i - move < 0 or j + move > 7:
															break


													# Съедает
													else:
														if 7 >= i - move >= 0 and 7 >= j + move >= 0:
															if step == all_chassmen[i-move][j+move][:5]:
																if [i-move, j+move] not in under_attack:
																	under_attack.append([i-move, j+move])
												move = 1



												# Ходы по одному ВВЕРХ
												if 7 >= j - move >= 0:
													while all_chassmen[i][j-move] == None:
														if [i, j-move] not in under_attack:
															under_attack.append([i, j-move])
														move += 1

														if j - move < 0:
															break


													# Съедает
													else:
														if 7 >= j - move >= 0:
															if step == all_chassmen[i][j-move][:5]:
																if [i, j-move] not in under_attack:
																	under_attack.append([i, j-move])
												move = 1


												# Ходы по одному ВНИЗ
												if 7 >= j + move >= 0:
													while all_chassmen[i][j+move] == None:
														if [i, j+move] not in under_attack:
															under_attack.append([i, j+move])
														move += 1

														if j + move > 7:
															break


													# Съедает
													else:
														if 7 >= j + move >= 0:
															if step == all_chassmen[i][j+move][:5]:
																if [i, j+move] not in under_attack:
																	under_attack.append([i, j+move])
												move = 1


												# Ходы по одному ВЛЕВО
												if 7 >= i - move >= 0:
													while all_chassmen[i-move][j] == None:
														if [i-move, j] not in under_attack:
															under_attack.append([i-move, j])
														move += 1

														if i - move < 0:
															break

													# Съедает
													else:
														if 7 >= i - move >= 0:
															if step == all_chassmen[i-move][j][:5]:
																if [i-move, j] not in under_attack:
																	under_attack.append([i-move, j])
												move = 1


												# Ходы по одному ВПРАВО
												if 7 >= i + move >= 0:
													while all_chassmen[i+move][j] == None:
														if [i+move, j] not in under_attack:
															under_attack.append([i+move, j])
														move += 1

														if i + move > 7:
															break

													# Съедает
													else:
														if 7 >= i + move >= 0:
															if step == all_chassmen[i+move][j][:5]:
																if [i+move, j] not in under_attack:
																	under_attack.append([i+move, j])



											# -------------------------------->> КОРОЛЬ <<--------------------------------
											elif all_chassmen[i][j] == "white_king" or all_chassmen[i][j] == "black_king":
												move = 1

												# Ход ВВЕРХ
												if 7 >= i >= 0 and 7 >= j - move >= 0:
													if all_chassmen[i][j-move] == None:
														if [i, j-move] not in under_attack:
															under_attack.append([i, j-move])

													# Съедает
													else:
														if 7 >= i >= 0 and 7 >= j - move >= 0:
															if step == all_chassmen[i][j-move][:5]:
																if [i, j-move] not in under_attack:
																	under_attack.append([i, j-move])


												# Ход ВНИЗ
												if 7 >= i >= 0 and 7 >= j + move >= 0:
													if all_chassmen[i][j+move] == None:
														if [i, j+move] not in under_attack:
															under_attack.append([i, j+move])

													# Съедает
													else:
														if 7 >= i >= 0 and 7 >= j + move >= 0:
															if step == all_chassmen[i][j+move][:5]:
																if [i, j+move] not in under_attack:
																	under_attack.append([i, j+move])


												# Ход ВЛЕВО
												if 7 >= i - move >= 0 and 7 >= j >= 0:
													if all_chassmen[i-move][j] == None:
														if [i-move, j] not in under_attack:
															under_attack.append([i-move, j])

													# Съедает
													else:
														if 7 >= i - move >= 0 and 7 >= j >= 0:
															if step == all_chassmen[i-move][j][:5]:
																if [i-move, j] not in under_attack:
																	under_attack.append([i-move, j])


												# Ход ВПРАВО
												if 7 >= i + move >= 0 and 7 >= j >= 0:
													if all_chassmen[i+move][j] == None:
														if [i+move, j] not in under_attack:
															under_attack.append([i+move, j])

													# Съедает
													else:
														if 7 >= i + move >= 0 and 7 >= j >= 0:
															if step == all_chassmen[i+move][j][:5]:
																if [i+move, j] not in under_attack:
																	under_attack.append([i+move, j])


												# Ход ВВЕРХ-ВЛЕВО
												if 7 >= i - move >= 0 and 7 >= j - move >= 0:
													if all_chassmen[i-move][j-move] == None:
														if [i-move, j-move] not in under_attack:
															under_attack.append([i-move, j-move])

													# Съедает
													else:
														if 7 >= i - move >= 0 and 7 >= j - move >= 0:
															if step == all_chassmen[i-move][j-move][:5]:
																if [i-move, j-move] not in under_attack:
																	under_attack.append([i-move, j-move])


												# Ход ВВЕРХ-ВПРАВО
												if 7 >= i + move >= 0 and 7 >= j - move >= 0:
													if all_chassmen[i+move][j-move] == None:
														if [i+move, j-move] not in under_attack:
															under_attack.append([i+move, j-move])

													# Съедает
													else:
														if 7 >= i + move >= 0 and 7 >= j - move >= 0:
															if step == all_chassmen[i+move][j-move][:5]:
																if [i+move, j-move] not in under_attack:
																	under_attack.append([i+move, j-move])


												# Ход ВНИЗ-ВЛЕВО
												if 7 >= i - move >= 0 and 7 >= j + move >= 0:
													if all_chassmen[i-move][j+move] == None:
														if [i-move, j+move] not in under_attack:
															under_attack.append([i-move, j+move])

													# Съедает
													else:
														if 7 >= i - move >= 0 and 7 >= j + move >= 0:
															if step == all_chassmen[i-move][j+move][:5]:
																if [i-move, j+move] not in under_attack:
																	under_attack.append([i-move, j+move])


												# Ход ВНИЗ-ВПРАВО
												if 7 >= i + move >= 0 and 7 >= j + move >= 0:
													if all_chassmen[i+move][j+move] == None:
														if [i+move, j+move] not in under_attack:
															under_attack.append([i+move, j+move])

													# Съедает
													else:
														if 7 >= i + move >= 0 and 7 >= j + move >= 0:
															if step == all_chassmen[i+move][j+move][:5]:
																if [i+move, j+move] not in under_attack:
																	under_attack.append([i+move, j+move])





							# Находим координаты короля для дальнейшей проверки доступности хода
							for u in range(8):
								for o in range(8):
									if all_chassmen[u][o] == "black_king":
										black_king_x = u
										black_king_y = o
									if all_chassmen[u][o] == "white_king":
										white_king_x = u
										white_king_y = o




							# Если король под вражеской атакой
							if [black_king_x, black_king_y] in under_attack or [white_king_x, white_king_y] in under_attack:

								attacked = 1
					
								# Перемещаем положение фигуры в списке фигур обратно, как было
								all_chassmen[x][y] = chassman1
								all_chassmen[active_cell[0]][active_cell[1]] = chassman2

								# Возвращаем стандартные цвета клеткам
								field_array[active_cell[0]][active_cell[1]] = 0
								turn_off.pop()


								# Дезактивируем активную клетку
								active_cell = None

								# Очищаем список доступных ходов
								available_moves = []

								# Звук ошибки
								error_sound = pygame.mixer.Sound("sounds/error.wav")
								pygame.mixer.Sound.play(error_sound)





					# Если игрок ПОХОДИЛ ПРАВИЛЬНО и НЕ ПОДВЕРГ КОРОЛЯ ШАХУ
					if True:
						if [x,y] in available_moves:


							# --------------->>> Махинации с рокировкой <<<-------------------

							# ------------- Рокировка БЕЛОГО КОРОЛЯ -------------
							if active_cell[2] == "white_king":

								if [active_cell[0],active_cell[1]] == [4, 7]:

									# --- Рокировка вправо ---
									if [x,y] == [6,7]:

										# Проверка не под шахом ли три клетки, на которых происходит перемещения короля
										for cell in [[4, 7], [5, 7], [6, 7]]:
											if cell in under_attack:

												# Перемещаем положение фигуры в списке фигур обратно, как было
												all_chassmen[x][y] = chassman1
												all_chassmen[active_cell[0]][active_cell[1]] = chassman2

												# Возвращаем стандартные цвета клеткам
												field_array[active_cell[0]][active_cell[1]] = 0
												turn_off.pop()


												# Дезактивируем активную клетку
												active_cell = None

												# Очищаем список доступных ходов
												available_moves = []

										# Если да, хоть одна из них под шахом, то отменяем ход
										if available_moves == []:
											break

										# Меняем местоположение фигур
										all_chassmen[7][7] = None
										all_chassmen[active_cell[0]][active_cell[1]] = None
										all_chassmen[x][y] = "white_king"
										all_chassmen[x-1][y] = "white_rook"

										castling[0] = "Done"


									# --- Рокировка влево ---
									elif [x,y] == [2,7]:

										# Проверка не под шахом ли три клетки, на которых происходит перемещения короля
										for cell in [[4, 7], [3, 7], [2, 7]]:
											if cell in under_attack:

												# Перемещаем положение фигуры в списке фигур обратно, как было
												all_chassmen[x][y] = chassman1
												all_chassmen[active_cell[0]][active_cell[1]] = chassman2

												# Возвращаем стандартные цвета клеткам
												field_array[active_cell[0]][active_cell[1]] = 0
												turn_off.pop()


												# Дезактивируем активную клетку
												active_cell = None

												# Очищаем список доступных ходов
												available_moves = []

										# Если да, хоть одна из них под шахом, то отменяем ход
										if available_moves == []:
											break

										# Меняем местоположение фигур
										all_chassmen[0][7] = None
										all_chassmen[active_cell[0]][active_cell[1]] = None
										all_chassmen[x][y] = "white_king"
										all_chassmen[x+1][y] = "white_rook"

										castling[0] = "Done"


							# ------------- Рокировка ЧЕРНОГО КОРОЛЯ -------------
							if active_cell[2] == "black_king":

								if [active_cell[0],active_cell[1]] == [4, 0]:

									# --- Рокировка вправо ---
									if [x,y] == [6,0]:

										# Проверка не под шахом ли три клетки, на которых происходит перемещения короля
										for cell in [[4, 0], [5, 0], [6, 0]]:
											if cell in under_attack:

												# Перемещаем положение фигуры в списке фигур обратно, как было
												all_chassmen[x][y] = chassman1
												all_chassmen[active_cell[0]][active_cell[1]] = chassman2

												# Возвращаем стандартные цвета клеткам
												field_array[active_cell[0]][active_cell[1]] = 0
												turn_off.pop()


												# Дезактивируем активную клетку
												active_cell = None

												# Очищаем список доступных ходов
												available_moves = []

										# Если да, хоть одна из них под шахом, то отменяем ход
										if available_moves == []:
											break

										# Меняем местоположение фигур
										all_chassmen[7][0] = None
										all_chassmen[active_cell[0]][active_cell[1]] = None
										all_chassmen[x][y] = "black_king"
										all_chassmen[x-1][y] = "black_rook"

										castling[1] = "Done"


									# --- Рокировка влево ---
									elif [x,y] == [2,0]:

										# Проверка не под шахом ли три клетки, на которых происходит перемещения короля
										for cell in [[4, 0], [3, 0], [2, 0]]:
											if cell in under_attack:

												# Перемещаем положение фигуры в списке фигур обратно, как было
												all_chassmen[x][y] = chassman1
												all_chassmen[active_cell[0]][active_cell[1]] = chassman2

												# Возвращаем стандартные цвета клеткам
												field_array[active_cell[0]][active_cell[1]] = 0
												turn_off.pop()


												# Дезактивируем активную клетку
												active_cell = None

												# Очищаем список доступных ходов
												available_moves = []

										# Если да, хоть одна из них под шахом, то отменяем ход
										if available_moves == []:
											break

										# Меняем местоположение фигур
										all_chassmen[0][0] = None
										all_chassmen[active_cell[0]][active_cell[1]] = None
										all_chassmen[x][y] = "black_king"
										all_chassmen[x+1][y] = "black_rook"

										castling[1] = "Done"


							# Ладьи делают ход, рокировка становится невозможной
							if active_cell[2] == "white_rook":
								castling[0] = "Done"
							if active_cell[2] == "black_rook":
								castling[1] = "Done"

							# Короли делают ход, рокировка становится невозможной
							if active_cell[2] == "white_king":
								castling[0] = "Done"
							if active_cell[2] == "black_king":
								castling[1] = "Done"
							#----------------------------------------------------------------


							# Если пешка сделала взятие на проходе
							if active_cell[2][6:] == "pawn":
								if active_cell[0] != x and take_on_the_aisle == True:
									all_chassmen[turn_off[1][0]][turn_off[1][1]] = None



							# Если белая пешка дошла до конца
							if active_cell[2] == "white_pawn" and y == 0:
								brave_pawn = [x, y]
							# Если черная пешка дошла до конца
							if active_cell[2] == "black_pawn" and y == 7:
								brave_pawn = [x, y]



							# Меняем цвет клетки, на которую ходим
							field_array[x][y] = 1

							# Записываем клеточки для дальнейшей их деактивации и возвращения к стандартному цвету
							turn_off.append([x,y])

							# Дезактивируем активную клетку
							active_cell = None

							# Очищаем список доступных ходов
							available_moves = []

							# Возвращаем взятие на проходе
							take_on_the_aisle = False

							# Возвращаем стандартные цвета клеткам
							if len(turn_off) == 4:

								# Тут ифы для случаев когда кто-то кого-то ест и встает на ту же клетку что была и у предыдущего ходившего
								if turn_off[3] != turn_off[0]:
									field_array[turn_off[0][0]][turn_off[0][1]] = 0	
								if turn_off[3] != turn_off[1]:
									field_array[turn_off[1][0]][turn_off[1][1]] = 0

								turn_off = [turn_off[2], turn_off[3]]

							# Переход хода
							if step == "white":
								step = "black"
							else:
								step = "white"

							# Звук хода фигуры
							pygame.mixer.Sound.play(step_sound)


			# Если передумал ходить выбранной активной клеткой
			if click[2] == 1:
				# Если есть активная клетка
				if active_cell != None:

					# Возвращаем стандартные цвета клеткам
					field_array[active_cell[0]][active_cell[1]] = 0
					turn_off.pop()


					# Дезактивируем активную клетку
					active_cell = None

					# Очищаем список доступных ходов
					available_moves = []



	# Отображаем все фигуры
	for x in range(8):
		for y in range(8):

			if all_chassmen[x][y] == "white_pawn":

				img_rect = imgs[0].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[0], img_rect)

			elif all_chassmen[x][y] == "black_pawn":

				img_rect = imgs[6].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[6], img_rect)

			elif all_chassmen[x][y] == "white_rook":

				img_rect = imgs[1].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[1], img_rect)

			elif all_chassmen[x][y] == "black_rook":

				img_rect = imgs[7].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[7], img_rect)

			elif all_chassmen[x][y] == "white_knight":

				img_rect = imgs[2].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[2], img_rect)

			elif all_chassmen[x][y] == "black_knight":

				img_rect = imgs[8].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[8], img_rect)

			elif all_chassmen[x][y] == "white_bishop":

				img_rect = imgs[3].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[3], img_rect)

			elif all_chassmen[x][y] == "black_bishop":

				img_rect = imgs[9].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[9], img_rect)

			elif all_chassmen[x][y] == "white_queen":

				img_rect = imgs[4].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[4], img_rect)

			elif all_chassmen[x][y] == "black_queen":

				img_rect = imgs[10].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[10], img_rect)

			elif all_chassmen[x][y] == "white_king":

				img_rect = imgs[5].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[5], img_rect)

			elif all_chassmen[x][y] == "black_king":

				img_rect = imgs[11].get_rect()
				img_rect.center = (initial_spot[0] + x * cell_width + 41, initial_spot[1] + y * cell_width + 41)

				screen.blit(imgs[11], img_rect)

	# Даем игроку превратить пешку в другую фигуру
	if brave_pawn != None:

		choice = choose_something(screen, initial_spot, step, imgs)

		if choice != None:
			all_chassmen[brave_pawn[0]][brave_pawn[1]] = choice
			brave_pawn = None

	# Если король под шахом 
	if attacked == 1:
		king_is_attacked(screen, initial_spot, [white_king_x, white_king_y], [black_king_x, black_king_y], step)

	return (field_array, active_cell, available_moves, all_chassmen, step, turn_off, castling, take_on_the_aisle, brave_pawn, attacked)