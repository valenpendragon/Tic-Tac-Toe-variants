def print_board(moves,size):
    '''
    This functions accepts a screen size. The blocks are 4 lines by 5 spaces
    inside the borders of the "square". The rows are (5*size) + 1 long. There
    are (6*size) + 1 columns per row. Each block has a coordinate block in 
    row 1 of the 4 rows.
    This function als0 requires moves, a dictionary of (player: set of 
    moves) combinations. The function uses this to identify non-empty cells.
    INPUT: integer size, dict player_moves {player's name : set of player moves}
    '''
    # First, we need to get the player names out of the dictionary.
    players = moves.keys()
    print players
    
    # We make the top/bottom border. For now, it will use Bs for borders.
    # border_char is a constant that is used to build the borders of the cells.
    h_border_char = '_'  # This is the horizontal character used.
    v_border_char = '|'  # This is the vertical character used.
    
    # reference_ruler_horiz allows us to check lengths and positions.
    reference_rule_horiz = '0123456789'*(size - 1)
    horiz_border = h_border_char*((6*size) + 1)
    print reference_rule_horiz
    # Next, we need to create and print coordinate blocks.
    print horiz_border
    for row in xrange(0,size):
        # coord_block (coordinate block) is where each cell's coordinates print out.
        # cells_row1 of each cell is the first line below the coord_block.
        # cells_row2 of each cell is the second line below the coord_block.
        # cells_row3 of each cell is the third (and last) line below the coord_block.
        # This initializes each line as the current row is constructed.
        coord_block = cells_row1 = cells_row2 = cells_row3 = v_border_char
        for col in xrange(0,size):
            new_cell_coord = "(" + str(row)+"," + str(col) + ")" + v_border_char
            coord_block = coord_block + new_cell_coord
            
            # Now, we need to know if the cell is empty.
            if ((row,col) in moves[players[0]]):
                # So, player1 has an X in the cell. This block creates it.
                new_cell_row1 = ' X X '+ v_border_char
                new_cell_row2 = '  X  '+ v_border_char
                new_cell_row3 = ' X X '+ v_border_char
            elif ((row,col) in moves[players[1]]):
                # player2 controls this cell. This block puts an O in it.
                new_cell_row1 = '  O  '+ v_border_char
                new_cell_row2 = ' O O '+ v_border_char
                new_cell_row3 = '  O  '+ v_border_char
            else: # The cell is empty. This block add an empty cell.
                new_cell_row1 = ' '*5 + v_border_char
                new_cell_row2 = ' '*5 + v_border_char
                new_cell_row3 = ' '*5 + v_border_char
            # Now, we concatenate the cell contents with the rest of the row.
            cells_row1 = cells_row1 + new_cell_row1
            cells_row2 = cells_row2 + new_cell_row2
            cells_row3 = cells_row3 + new_cell_row3
        print coord_block
        print cells_row1
        print cells_row2
        print cells_row3
        print horiz_border
    return
