import time

symbols = {'X': 'wall',
           'W': 'water',
           'M': 'monster',
           'E': 'end',
           'P': 'player',
           ' ': 'open corridor'}

def read_maze(maze_file='MAZE.txt'):
    """Opens, formats and reads maze"""
    f = open(maze_file, 'r')
    maze = f.readlines()
    del f
    new_maze = [line.replace('\n', '') for line in maze]
    return new_maze

def maze_player():
    """Navigates through maze"""
    maze_player = raw_input("Enter your name:")
    return maze_player

def find_symbol(symbol):
    """Finds start and end point"""
    row_coor = 0
    for row in maze:
        if symbol in row:
            return [row_coor, row.find(symbol)]
        else:
            row_coor += 1

def get_symbol(coor, maze):
    """Returns symbol at given coordinate"""
    x, y = coor
    if x < 0 or y < 0:
        return "X"
    else:
        return maze[x][y]

def surroundings(coor, maze):
    """Returns surroundings"""
    x, y = coor
    surrounds = {'N': get_symbol([x-1, y], maze),
                 'S': get_symbol([x+1, y], maze),
                 'E': get_symbol([x, y+1], maze),
                 'W': get_symbol([x, y-1], maze)}
    return surrounds

def message(surrounds):    
    return """To the north you see a {},
to the south you see a {},
to the east you see a {},
to the west you see a {}.
           """.format(symbols[surrounds['N']],
                      symbols[surrounds['S']],
                      symbols[surrounds['E']],
                      symbols[surrounds['W']])

def valid_moves(surrounds):
    """returns the valid move directions for a given surrounds

    >>> valid_moves({'N': 'X', 'S': 'X', 'E': 'X', 'W': 'E'})
    ['W',]

    """
    passable_terrain = (' ', 'E')
    valid = []
    for direction in surrounds:
        if surrounds[direction] in passable_terrain:
            valid.append(direction)
    return valid

def player_move_choice(surrounds):
    choice = None
    while choice is None:
        player_move = raw_input("Enter 'N', 'S', 'E' or 'W'")
        if player_move.upper() in valid_moves(surrounds):
            choice = player_move.upper()
        elif player_move.upper() in ('N', 'E', 'S', 'W'):
            if surrounds[player_move.upper()] == 'X':
                print("Your path is blocked by a wall! Choose another way.")
            else:
                print("Your path is blocked! Choose another way.")
        else:
            print("Invalid choice!")
    return player_move

def move_player(move_direction, player_coor):
    """moves player in given direction

    >>> move_player('E', [0, 0])
    [0, 1]

    >>> move_player('N', [1, 1])
    [0, 1]

    """
    x, y = player_coor
    moves = {'N': [x-1, y],
             'S': [x+1, y], 
             'E': [x, y+1], 
             'W': [x, y-1]}
    return moves[move_direction.upper()]
    
## Main

maze = read_maze()
player_name = maze_player()
print("Welcome {}!".format(player_name))
player_coor = find_symbol("P")

start = time.time()
while get_symbol(player_coor, maze) != 'E':
    surrounds = surroundings(player_coor, maze)
    print(message(surrounds))
    move_direction = player_move_choice(surrounds)
    player_coor = move_player(move_direction, player_coor)
stop = time.time()
print("You escaped!")
print("It took you {} to escape!".format(stop-start))

##row_coor = 0
##for row in maze:
##    if "s" in row:
##        print(row_coor, row.find("s"))
##    else:
##        row_coor += 1
##
##find_symbol("s") -> [1, 0]
#if " " == W:
    #print "You fell in the water! Turn around!"
#if " " == M:
    #print "There is a monster ahead! Go back the other way!"
#if " " == X:
    #print "You hit a wall."
#if " " == E:
    #print "You made it to the end of the maze!"


