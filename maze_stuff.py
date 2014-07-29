Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open('maze.txt', 'r')

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open('maze.txt', 'r')
IOError: [Errno 2] No such file or directory: 'maze.txt'
>>> f = open('P:\gitprojects\Final_Project\MAZE.txt', 'r')
>>> print f
<open file 'P:\gitprojects\Final_Project\MAZE.txt', mode 'r' at 0x02A58860>
>>> print file.read()

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print file.read()
TypeError: descriptor 'read' of 'file' object needs an argument
>>> print file.read(f)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
s                            X
XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX
      X X       XXXXXXX    X X    X      w
      X X       X     X    X X    X XXXXXX 
  XXXXX XXXXXXXXX XXX X    X X    X X
  X               X X X XXXX XXXXXX XXXXXX
  X XXXXXXXXXXX XXX X X X                X  
  X X         X X   X XXXXXXXXXXXX XXXXXXX  
  XWX         X X   X            X X   X X
              X X   X XXXXXXXXXX X X   X X
              X X   X X        X X X   X X
  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X
  X                                      X
  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX 
  X X    XMX  X X     X X        X X   
  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX
  X XXXXXX X  X X  M                     X
  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X
  XXXXXXXXXX  X       W                X X
              XXXXXXXXX                XEX
>>> print file.readlines(5)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print file.readlines(5)
TypeError: descriptor 'readlines' requires a 'file' object but received a 'int'
>>> print file.readlines()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print file.readlines()
TypeError: descriptor 'readlines' of 'file' object needs an argument
>>> print file.readlines(f)
[]
>>> print file.read(f)

>>> f = open('P:\gitprojects\Final_Project\MAZE.txt', 'r')
>>> print file.read(f)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
s                            X
XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX
      X X       XXXXXXX    X X    X      w
      X X       X     X    X X    X XXXXXX 
  XXXXX XXXXXXXXX XXX X    X X    X X
  X               X X X XXXX XXXXXX XXXXXX
  X XXXXXXXXXXX XXX X X X                X  
  X X         X X   X XXXXXXXXXXXX XXXXXXX  
  XWX         X X   X            X X   X X
              X X   X XXXXXXXXXX X X   X X
              X X   X X        X X X   X X
  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X
  X                                      X
  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX 
  X X    XMX  X X     X X        X X   
  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX
  X XXXXXX X  X X  M                     X
  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X
  XXXXXXXXXX  X       W                X X
              XXXXXXXXX                XEX
>>> print file.readlines(f)
[]
>>> f
<open file 'P:\gitprojects\Final_Project\MAZE.txt', mode 'r' at 0x02ABD808>
>>> f.seek(0)
>>> maze = f.readlines()
>>> maze
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n', 's                            X\n', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX\n', '      X X       XXXXXXX    X X    X      w\n', '      X X       X     X    X X    X XXXXXX \n', '  XXXXX XXXXXXXXX XXX X    X X    X X\n', '  X               X X X XXXX XXXXXX XXXXXX\n', '  X XXXXXXXXXXX XXX X X X                X  \n', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  \n', '  XWX         X X   X            X X   X X\n', '              X X   X XXXXXXXXXX X X   X X\n', '              X X   X X        X X X   X X\n', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X\n', '  X                                      X\n', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX \n', '  X X    XMX  X X     X X        X X   \n', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX\n', '  X XXXXXX X  X X  M                     X\n', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X\n', '  XXXXXXXXXX  X       W                X X\n', '              XXXXXXXXX                XEX']
>>> for line in maze:
	print(line)

	
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

s                            X

XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX

      X X       XXXXXXX    X X    X      w

      X X       X     X    X X    X XXXXXX 

  XXXXX XXXXXXXXX XXX X    X X    X X

  X               X X X XXXX XXXXXX XXXXXX

  X XXXXXXXXXXX XXX X X X                X  

  X X         X X   X XXXXXXXXXXXX XXXXXXX  

  XWX         X X   X            X X   X X

              X X   X XXXXXXXXXX X X   X X

              X X   X X        X X X   X X

  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X

  X                                      X

  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX 

  X X    XMX  X X     X X        X X   

  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX

  X XXXXXX X  X X  M                     X

  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X

  XXXXXXXXXX  X       W                X X

              XXXXXXXXX                XEX
>>> for line in maze:
	print(line.strip())

	
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
s                            X
XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX
X X       XXXXXXX    X X    X      w
X X       X     X    X X    X XXXXXX
XXXXX XXXXXXXXX XXX X    X X    X X
X               X X X XXXX XXXXXX XXXXXX
X XXXXXXXXXXX XXX X X X                X
X X         X X   X XXXXXXXXXXXX XXXXXXX
XWX         X X   X            X X   X X
X X   X XXXXXXXXXX X X   X X
X X   X X        X X X   X X
XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X
X                                      X
X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX
X X    XMX  X X     X X        X X
X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX
X XXXXXX X  X X  M                     X
X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X
XXXXXXXXXX  X       W                X X
XXXXXXXXX                XEX
>>> ================================ RESTART ================================
>>> f = open('P:\gitprojects\Final_Project\MAZE.txt', 'r')
>>> maze = f.readlines()
>>> for line in maze:
	print(line)

	
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            

s                            X            

XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX

      X X       XXXXXXX    X X    X      w

      X X       X     X    X X    X XXXXXX 

  XXXXX XXXXXXXXX XXX X    X X    X X     

  X               X X X XXXX XXXXXX XXXXXX

  X XXXXXXXXXXX XXX X X X                X  

  X X         X X   X XXXXXXXXXXXX XXXXXXX  

  XWX         X X   X            X X   X X

              X X   X XXXXXXXXXX X X   X X

              X X   X X        X X X   X X

  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X

  X                                      X

  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX 

  X X    XMX  X X     X X        X X      

  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX

  X XXXXXX X  X X  M                     X

  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X

  XXXXXXXXXX  X       W                X X

              XXXXXXXXX                XEX
>>> for line in maze:
	print(line.strip())

	
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
s                            X
XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX
X X       XXXXXXX    X X    X      w
X X       X     X    X X    X XXXXXX
XXXXX XXXXXXXXX XXX X    X X    X X
X               X X X XXXX XXXXXX XXXXXX
X XXXXXXXXXXX XXX X X X                X
X X         X X   X XXXXXXXXXXXX XXXXXXX
XWX         X X   X            X X   X X
X X   X XXXXXXXXXX X X   X X
X X   X X        X X X   X X
XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X
X                                      X
X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX
X X    XMX  X X     X X        X X
X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX
X XXXXXX X  X X  M                     X
X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X
XXXXXXXXXX  X       W                X X
XXXXXXXXX                XEX
>>> for line in maze:
	print(line.replace('\n', ''))

	
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            
s                            X            
XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX
      X X       XXXXXXX    X X    X      w
      X X       X     X    X X    X XXXXXX 
  XXXXX XXXXXXXXX XXX X    X X    X X     
  X               X X X XXXX XXXXXX XXXXXX
  X XXXXXXXXXXX XXX X X X                X  
  X X         X X   X XXXXXXXXXXXX XXXXXXX  
  XWX         X X   X            X X   X X
              X X   X XXXXXXXXXX X X   X X
              X X   X X        X X X   X X
  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X
  X                                      X
  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX 
  X X    XMX  X X     X X        X X      
  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX
  X XXXXXX X  X X  M                     X
  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X
  XXXXXXXXXX  X       W                X X
              XXXXXXXXX                XEX
>>> maze
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            \n', 's                            X            \n', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX\n', '      X X       XXXXXXX    X X    X      w\n', '      X X       X     X    X X    X XXXXXX \n', '  XXXXX XXXXXXXXX XXX X    X X    X X     \n', '  X               X X X XXXX XXXXXX XXXXXX\n', '  X XXXXXXXXXXX XXX X X X                X  \n', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  \n', '  XWX         X X   X            X X   X X\n', '              X X   X XXXXXXXXXX X X   X X\n', '              X X   X X        X X X   X X\n', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X\n', '  X                                      X\n', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX \n', '  X X    XMX  X X     X X        X X      \n', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX\n', '  X XXXXXX X  X X  M                     X\n', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X\n', '  XXXXXXXXXX  X       W                X X\n', '              XXXXXXXXX                XEX']
>>> maze = [line.replace('\n', '') for line in maze]
>>> maze
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
>>> for line in maze:
	print(maze)

	
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
>>> ================================ RESTART ================================
>>> 
>>> maze>>> f = open('P:\gitprojects\Final_Project\MAZE.txt', 'r')
>>> 
SyntaxError: invalid syntax
>>> maze
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            \n', 's                            X            \n', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX\n', '      X X       XXXXXXX    X X    X      w\n', '      X X       X     X    X X    X XXXXXX \n', '  XXXXX XXXXXXXXX XXX X    X X    X X     \n', '  X               X X X XXXX XXXXXX XXXXXX\n', '  X XXXXXXXXXXX XXX X X X                X  \n', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  \n', '  XWX         X X   X            X X   X X\n', '              X X   X XXXXXXXXXX X X   X X\n', '              X X   X X        X X X   X X\n', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X\n', '  X                                      X\n', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX \n', '  X X    XMX  X X     X X        X X      \n', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX\n', '  X XXXXXX X  X X  M                     X\n', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X\n', '  XXXXXXXXXX  X       W                X X\n', '              XXXXXXXXX                XEX']
>>> new_maze
['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ', 's                            X            ', 'XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX', '      X X       XXXXXXX    X X    X      w', '      X X       X     X    X X    X XXXXXX ', '  XXXXX XXXXXXXXX XXX X    X X    X X     ', '  X               X X X XXXX XXXXXX XXXXXX', '  X XXXXXXXXXXX XXX X X X                X  ', '  X X         X X   X XXXXXXXXXXXX XXXXXXX  ', '  XWX         X X   X            X X   X X', '              X X   X XXXXXXXXXX X X   X X', '              X X   X X        X X X   X X', '  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X', '  X                                      X', '  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX ', '  X X    XMX  X X     X X        X X      ', '  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX', '  X XXXXXX X  X X  M                     X', '  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X', '  XXXXXXXXXX  X       W                X X', '              XXXXXXXXX                XEX']
>>> for line in new_maze:
	print(line)

	
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            
s                            X            
XXXXXXX XXXXXXXXXXXXXXXXXXXX X    XXXXXXXX
      X X       XXXXXXX    X X    X      w
      X X       X     X    X X    X XXXXXX 
  XXXXX XXXXXXXXX XXX X    X X    X X     
  X               X X X XXXX XXXXXX XXXXXX
  X XXXXXXXXXXX XXX X X X                X  
  X X         X X   X XXXXXXXXXXXX XXXXXXX  
  XWX         X X   X            X X   X X
              X X   X XXXXXXXXXX X X   X X
              X X   X X        X X X   X X
  XXXXXXXXXXXXX XXXXX XXXXXXXXXX X XXXXX X
  X                                      X
  X XXXXXXXXXXX XXXXXXX XXXXXXXXXX XXXXXXX 
  X X    XMX  X X     X X        X X      
  X X    X X  X X  XXXX XXXXXXXXXX XXXXXXX
  X XXXXXX X  X X  M                     X
  X        X  X XXXXXXXXXXXXXXXXXXXXXXXX X
  XXXXXXXXXX  X       W                X X
              XXXXXXXXX                XEX
>>> 
