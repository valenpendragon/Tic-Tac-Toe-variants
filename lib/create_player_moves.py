def create_player_moves(size):
    '''
    This function takes an integer size. From there, it will prompt the players for how many players
    actually want to play. It will allow up to size - 1 to give the players some chance of winning.
    It will return an initialized player_moves dictionary. This dictionary maps the player's name
    to a set of tuples (x,y) representing the two-dimensional coordinates of every move the player
    will make in the game. player_moves does that for every player in the game.
    INPUT: integer size for the size of the size x size board
    OUTPUT: dictionary player_moves, initialized with all player names mapped to empty sets ready to 
    receive their moves.
    '''
    # Initialize the player_moves dictionary.
    player_moves = {}
    max_players = size - 1
    print "To increase the likelihood of a player winning, this game limits the number of"
    print "players to one less than the size of the board."
    num_players = 0
    while (num_players < 2) or (num_players >= size):
        if (size == 3):
            print "Due to the small size of the board (3x3), this game will default to 2 players."
            num_players = 2
        else:
            new_num = raw_input("Please choose a number between 2 and {0}: ".format(max_players))
            num_players = int(new_num)
    # Ordinals in Python seem to be a work in progress. Since the board is currently limited
    # to 9 squares at most, this limits players ordinals to 1st through 8th (for now). So, we
    # initialize a good list to use when addressing the players.
    ordinal_words = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
    
    # Now, we initialize the player_moves dictionary. We need a name for each player, which
    # will be added to the keys of the dictionary. Each name will be mapped to a set of tuples
    # (currently empty), that stores that players moves throughout the game.
    for num in xrange(0, num_players):
        player = raw_input("What is the name of the "+ordinal_words[num]+" player? ")
        player_moves[player] = set()
        print "Confirming that the "+ordinal_words[num]+ " will be "+player
    print player_moves
    ready_to_play = 'n'
    while (ready_to_play != 'y') and (ready_to_play != 'Y') and (ready_to_play != 'yes'):
        ready_to_play = raw_input("Are all of the players ready to start? ")
    return player_moves
