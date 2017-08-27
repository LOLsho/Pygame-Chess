# Функция создания списка всех фигур


def create_all_chassmen():

	all_chassmen = [[None] * 8 for j in range(8)]
	for x in range(8):
		for y in range(8):
			if y == 1:
				all_chassmen[x][y] = "black_pawn"
			elif y == 6:
				all_chassmen[x][y] = "white_pawn"
			elif x == 0 and y == 0 or x == 7 and y == 0:
				all_chassmen[x][y] = "black_rook"
			elif x == 0 and y == 7 or x == 7 and y == 7:
				all_chassmen[x][y] = "white_rook"
			elif x == 1 and y == 0 or x == 6 and y == 0:
				all_chassmen[x][y] = "black_knight"
			elif x == 1 and y == 7 or x == 6 and y == 7:
				all_chassmen[x][y] = "white_knight"
			elif x == 2 and y == 0 or x == 5 and y == 0:
				all_chassmen[x][y] = "black_bishop"
			elif x == 2 and y == 7 or x == 5 and y == 7:
				all_chassmen[x][y] = "white_bishop"
			elif x == 3 and y == 0:
				all_chassmen[x][y] = "black_queen"
			elif x == 3 and y == 7:
				all_chassmen[x][y] = "white_queen"
			elif x == 4 and y == 0:
				all_chassmen[x][y] = "black_king"
			elif x == 4 and y == 7:
				all_chassmen[x][y] = "white_king"

	return all_chassmen