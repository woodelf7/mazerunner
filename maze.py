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

maze = read_maze()
player_name = maze_player()
print("Welcome {}!".format(player_name))
for line in maze:
    print(line)
#if " " == W:
    #print "You fell in the water! Turn around!"
#if " " == M:
    #print "There is a monster ahead! Go back the other way!"
#if " " == X:
    #print "You hit a wall."
#if " " == E:
    #print "You made it to the end of the maze!"

