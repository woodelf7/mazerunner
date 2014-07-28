f = open('MAZE.txt', 'r')
maze = f.readlines()
del f

new_maze = [line.replace('\n', '') for line in maze]
