from collections import deque

#node data type
class Node(object):
	ancestor = None
	distance = 0
	def __init__(self, coordinates):
		self.coordinates = coordinates

##read in file##
filename = raw_input("filename: ")
mazeread = open(filename, 'r')
maze = mazeread.readlines()
def remove_newline(x):
	return x.rstrip("\r\n")

def string_to_list(x):
	return list(x)

##turn maze into 2D matrix of chars
maze = map(remove_newline, maze)
maze = map(string_to_list, maze)

#save size of maze
columns = len(maze[0])
rows = len(maze)

#determine walls, paths, start and end
#start = raw_input("start char: ")
#end = raw_input("end char: ")
#wall = raw_input("wall char: ")
#path = raw_input("path char: ") 
st = 's'
end = 'f'
wall = '|'
path = 'x'

#find start
startCoord = []
for row in maze:
	for char in row:
		if char == st:
			startCoord = row
			break
			
#indices of start matrix
rowSt = maze.index(startCoord)
colSt = maze[rowSt].index(st)

#make start a node
start = Node([rowSt, colSt])

#initialize visited matrix
visited = [[False for x in range(columns)] for x in range(rows)]

##initialize queue and endNode
queue = deque()
endNode = start
#######BFS##########
def bfs(start):
	queue.append(start)
	while len(queue) > 0 and endNode is start: #or find finish
		current = queue.popleft()
		row = current.coordinates[0]
		col = current.coordinates[1]
		visited[row][col] = True
		if row > 0 and not visited[row - 1][col] and maze[row - 1][col] is not wall:
			check_neighbors([row - 1, col], current)
		if row < rows - 1 and not visited[row + 1][col] and maze[row + 1][col] is not wall:
			check_neighbors([row + 1, col], current)
		if col > 0 and not visited[row][col - 1] and maze[row][col - 1] is not wall:
			check_neighbors([row, col - 1], current)
		if col < columns - 1 and not visited[row][col + 1] and maze[row][col + 1] is not wall:
			check_neighbors([row, col + 1], current)
	if len(queue) == 0: ### there is not a path
		return None
	else:
		return endNode

##to create a node of each valid neighbor
def check_neighbors(coords, current):
	add = Node(coords)
	add.ancestor = current
	add.distance = current.distance + 1
	queue.append(add)
	visited[coords[0]][coords[1]] == True
	if maze[coords[0]][coords[1]] == end:
		global endNode
		endNode = add

result = bfs(start)

##find the path
stack = []
current = result
while current.ancestor is not None:
	stack.append(current)
	current = current.ancestor

##print out the path
print "start:", current.coordinates
while len(stack) > 1:
	print stack.pop().coordinates
print "end:", stack.pop().coordinates