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

## Main

maze = read_maze()
player_name = maze_player()
print("Welcome {}!".format(player_name))
player = find_symbol("P")
print(player)
print(surroundings(player, maze))


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


