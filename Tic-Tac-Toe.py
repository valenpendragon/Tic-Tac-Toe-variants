print "Hello. You have accessed Tic Tac Toe."
print "The default board is 3x3 and the winner must control three"
print "spaces in a row, column, or diagonal to win."
option = raw_input("You may specify a larger board now, if you like. (y/n):")
if ((option == 'y') or (option == 'Y') or (option == 'yes')):
    # new_size is a str that will be passed to size as an integer.
    new_size = raw_input("The boards are square. Choose a size between 3 and 9:")
    size = int(new_size)
    if size in range(3,10):
        print "Thank you. Confirming that you wish a "+new_size+'x'+new_size+' board.'
    else:
        print new_size+' is an invalid board size. Exiting.'
        quit()
else:
    print "Board will be the default size of 3x3"
    size = 3
# The size has been initialized. Next, it asks for player names. These will be
# used to initial the dictionary player_moves. This dictionary is in the form
# {'player1' : {set of moves}, 'player2' : {set of moves}}. These sets are key
# to refreshing the board, determining wins, etc.
player1 = raw_input("What is the name of the first player?")
print "Thank you. Confirming that the first player is "+player1
player2 = raw_input("what is the name of the second player?")
print "Thank you. Confirming that the second player is "+player2

print player1+' and '+player2+', I am initializing the game for you.'
print "This will just take a moment."
