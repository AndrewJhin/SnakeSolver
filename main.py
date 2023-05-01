from snek import *
from time import sleep


if __name__ == "__main__":
	#ptr to board
	board = init_board()
	
	play_on = 1
	show_board(board)
	axis = AXIS_INIT
	direction = DIR_INIT
	bs = BOARD_SIZE

	loop = 0
	while (play_on):
		x_coord, y_coord = board[0].snek[0].head[0].coord[x], \
						   board[0].snek[0].head[0].coord[y]
		'''
		if x_coord == 0 and y_coord == 0:
			direction = DOWN
			axis = AXIS_Y
		'''
		if bs%2 == 0:
			if x_coord%2 == 0:
				if y_coord == bs - 1:
					direction = RIGHT
					axis = AXIS_X
				elif y_coord == 0 and x_coord != 0:
					direction = LEFT
					axis = AXIS_X
				else:
					direction = DOWN
					axis = AXIS_Y	
			if x_coord%2 == 1:
				if y_coord == 1 and x_coord != bs - 1:
					direction = RIGHT
					axis = AXIS_X
				elif y_coord == 0 and x_coord != 0:
					direction = LEFT
					axis = AXIS_X
				else:
					direction = UP
					axis =AXIS_Y 

		
		if bs%2 == 1:
			if y_coord == bs - 1:
				if x_coord%2 == 0:
					direction = RIGHT
					axis = AXIS_X
				if x_coord%2 == 1 and y_coord%2 == 0:
					direction = UP
					axis = AXIS_Y
			if y_coord == bs - 2:
				if x_coord%2 == 1:
					direction = RIGHT
					axis = AXIS_X
				if x_coord%2 == 0 and y_coord%2 == 1:
					direction = DOWN
					axis = AXIS_Y	
			if y_coord%2 == 0 and y_coord != bs - 1:
				if x_coord != bs - 1 and x_coord != 0:
					direction = LEFT
					axis = AXIS_X
				elif x_coord == 0:
					direction = DOWN
					axis = AXIS_Y
				else:
					direction = UP
					axis = AXIS_Y
			if y_coord%2 == 1 and y_coord != bs - 2:
				if x_coord != bs - 1 and x_coord != bs - 2:
					direction = RIGHT
					axis = AXIS_X
				elif x_coord == bs - 2:
					direction = DOWN
					axis = AXIS_Y
				else:
					direction = UP
					axis = AXIS_Y
			if x_coord == bs - 1 and y_coord == bs - 2:
				direction = UP
				axis = AXIS_Y
			if x_coord == bs - 1 and y_coord == 0:
				direction = LEFT
				axis = AXIS_X
			if x_coord == 0 and y_coord == 0:
				direction = DOWN
				axis = AXIS_Y
			if loop%2 == 1:
				if x_coord == bs - 2 and y_coord == bs - 1:
					direction = RIGHT
					axis = AXIS_X
				if x_coord == 0 and y_coord == 0:
					loop += 1
			if x_coord == bs - 1 and y_coord == bs - 1:
				direction = UP
				axis = AXIS_Y
		
	


		#indexing at 0 dereferences the pointer
		
		
		#I just realized this is redundantly written
		#Oh well...
		
		play_on = advance_frame(axis, direction, board)
		show_board(board)
		sleep(0.0001)
	
	#pass by reference to clean memory	
	end_game(byref(board))
