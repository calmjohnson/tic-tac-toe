print """
			*-----------------------------------------------------*
			|           	 TIC TAC TOE                          |
			|            Developed By Calmjohnson                 |
			|     github: https://github.com/calmjohnson          |
			|  repo: https://github.com/calmjohnson/tic-tac-toe   |
			|                                                     |
			|                                                     |
			|    How To Play:                                     |
			|    Enter the number on the spot you want to mark    |
			|                                                     |
			*-----------------------------------------------------*
"""
squares = [0,1,2,3,4,5,6,7,8,9] # the squares, added '0' so i can use square[N] 

choose_able = ['1','2','3','4','5','6','7','8','9'] # the player can only choose from this list of numbers


def board(): #function to draw the board
	print "\t\t\t\t\t     |     |     "
	
	print "\t\t\t\t\t  %s  |  %s  |  %s  " % (squares[1], squares[2], squares[3])
	
	print "\t\t\t\t\t_____|_____|_____"
	
	print "\t\t\t\t\t     |     |     "
	
	print "\t\t\t\t\t  %s  |  %s  |  %s  " % (squares[4], squares[5], squares[6])
	
	print "\t\t\t\t\t_____|_____|_____"
	
	print "\t\t\t\t\t     |     |     "
	
	print "\t\t\t\t\t  %s  |  %s  |  %s  " % (squares[7], squares[8], squares[9])
	
	print "\t\t\t\t\t     |     |     "

"""This function checks game status by comparing the squares, horizontally, vertically and diagonally
returns 1 when three squares marches which means game has ended with a winner
returns 0 when all squares have been marked which means game has ended without a winner
returns -1 when there is no march and some squares are un-marked which means game is still on"""

def check_win():
	if squares[1] == squares[2] and squares[2] == squares[3]:
		return 1
	
	elif squares[4] == squares[5] and squares[5] == squares[6]:
		return 1
	
	elif squares[7] == squares[8] and squares[8] == squares[9]:
		return 1
	
	elif squares[1] == squares[4] and squares[4] == squares[7]:
		return 1
	
	elif squares[2] == squares[5] and squares[5] == squares[8]:
		return 1
	
	elif squares[3] == squares[6] and squares[6] == squares[9]:
		return 1
	
	elif squares[1] == squares[5] and squares[5] == squares[9]:
		return 1
	
	elif squares[3] == squares[5] and squares[5] == squares[7]:
		return 1
	
	elif squares[1] != 1 and squares[2] != 2 and squares[3] != 3 and squares[4] != 4 and squares[5] != 5 and squares[6] != 6 and squares[7] != 7 and squares[8] != 8 and squares[9] != 9:
		return 0
	
	else:
		return -1

board()

player = 1

while check_win() == -1:
	
	print "Player %d turn" % player,
	choice = raw_input(">>> ")
	
	if choice in choose_able and squares[int(choice)] == int(choice):#makes sure the player enters a number from 1 to 9 and the square isn't marked
		if player == 1:
			mark = 'X'
			player += 1 # switch to player 2
		else:
			mark = 'O'
			player -= 1 # switch to player 1
		
		squares[int(choice)] = mark # mark the square
	
	else:
		print "Invalid Move!" # the current player would have to choose anothe square
	
	board()
	
if check_win() == 0:
	print """
			*-----------------------------------------------------*
			|                                                     |
			|           	 Game Over... It's a TIE!             |
			|                                                     |
			*-----------------------------------------------------*
	"""
else:
	if player == 1:
		player = "TWO"
	else:
		player = "ONE"
		
	print """
			*-----------------------------------------------------*
			|                                                     |
			|           Game Over... player %s won!              |
			|                                                     |
			*-----------------------------------------------------*
	""" % player
