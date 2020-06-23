game_array = [[0, 0, 0], 
			  [0, 0, 0], 
			  [0, 0, 0],]
def game_board(game_map, value=0, row=0, column=0):
	try:
		game_map[row][column]=value
		print("   a  b  c")
		for count, array in enumerate(game_map):
			print (count,array)
		return game_map
	except IndexError as e:
		print("Error: Make sure you give row/column as 0, 1 and 2",e)
	except Exception as e:
		print("Spmeting went terribly wrong!",e)			
game_array=game_board(game_array,value=1,row=3,column=1)
game_array=game_board(game_board,value=1,row=3,column=1)
