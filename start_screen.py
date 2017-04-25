def start_screen(size=3):
    '''
    This functions accepts a screen size, defaulting to 3 if not specified.
    The blocks are 4 lines by 5 spaces inside the borders of the "square".
    The rows are (5*size) + 1 long. There are (6*size) + 1 columns per row.
    Each block has a coordinate block in row 1 of the 4 rows.
    INPUT: integer size, defaults to 3
    '''
    # First, we make the top/bottom border. For now, it will use Bs for borders.
    # border_char is a constant that is used to build the borders of the cells.
    border_char = 'B'
    # reference_ruler_horiz allows us to check lengths and positions.
    reference_rule_horiz = '0123456789'*(size - 1)
    horiz_border = border_char*((5*size) + 1)
    print reference_rule_horiz
    print horiz_border
    # Next, we need to create and print coordinate blocks.
    for row in xrange(0,size):
        # coord_block (coordinate block) is where each cell's coordinates print out.
        # cells_row1 of each cell is the first line below the coord_block.
        # cells_row2 of each cell is the second line below the coord_block.
        # cells_row3 of each cell is the third (and last) line below the coord_block.
        # This initializes each line as the current row is constructed.
        coord_block = cells_row1 = cells_row2 = cells_row3 = border_char
        for col in xrange(0,size):
            new_cell_coord = "(" + str(row)+"," + str(col) + ")" + border_char
            coord_block = coord_block + new_cell_coord
            # Create the empty cells
            new_cell_row1 = ' '*5 + border_char
            cells_row1 = cells_row1 + new_cell_row1
            new_cell_row2 = ' '*5 + border_char
            cells_row2 = cells_row2 + new_cell_row2
            new_cell_row3 = ' '*5 + border_char
            cells_row3 = cells_row3 + new_cell_row3
        print coord_block
        print cells_row1
        print cells_row2
        print cells_row3
        print horiz_border
    return
