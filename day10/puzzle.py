# Open file, then translate into a list of lists
# Each tile of area_map can be accessed via area_map[y][x] (y and x starting at 0)
with open('puzzle-input.txt') as f:
    area_map = [*map(lambda l: [c for c in l if c != '\n'], f.readlines())]

area_map_height = len(area_map)
area_map_width = len(area_map[0])

# Search for starting point
start = None
for y, line in enumerate(area_map):
    if 'S' in line:
        x = line.index('S')
        start = (line.index('S'), y)
        break

pipes = {
    '|': ['N', 'S'],            # is a vertical pipe connecting north and south.
    '-': ['E', 'W'],            # is a horizontal pipe connecting east and west.
    'L': ['N', 'E'],            # is a 90-degree bend connecting north and east.
    'J': ['N', 'W'],            # is a 90-degree bend connecting north and west.
    '7': ['S', 'W'],            # is a 90-degree bend connecting south and west.
    'F': ['S', 'E'],            # is a 90-degree bend connecting south and east.
    'S': ['E', 'W', 'N', 'S']   # starting point can connect to all pipes.
}

opposing_directions = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

# Starting to find the path 
path = [[start]]
discovered = [start]

# print(start)

def find_neighboors(node):
    #print('find neighboors of:')
    #print(node)
    pipe_neighboors = []
    pipe_type = area_map[node[1]][node[0]]
    connected_directions = pipes[pipe_type]
    for direction in connected_directions:
        x,y = None, None
        type = None

        if direction == 'N' and node[1] > 0:
            x,y = (node[0], node[1]-1)
        if direction == 'S' and node[1] < area_map_height-1:
            x,y = (node[0], node[1]+1)
        if direction == 'E' and node[0] < area_map_width-1:
            x,y = (node[0]+1, node[1])
        if direction == 'W' and node[0] > 0:
            x,y = (node[0]-1, node[1])
        
        if (x,y) != (None,None) and (x,y) not in discovered:
            type = area_map[y][x]
            if type in pipes.keys() and opposing_directions[direction] in pipes[type]:
                pipe_neighboors += [(x,y)]
    
    #print('found:')
    #print(pipe_neighboors)
    return pipe_neighboors


end = False
while end == False:
    added_path = []
    #print('starting path:')
    #print(path)
    for node in path[-1]:
        found = find_neighboors(node)
        if len(found) > 0:
            added_path += found
            discovered += found
    if len(added_path) > 0:
        #print('added path:')
        #print(added_path)
        path += [added_path]
    if len(added_path) <= 1:
        end = True
    #print('ending path:')
    #print(path)
    #print('----------------------------')

print('farthest point:')
print(len(path[1::]))

# Puzzle 2 we need to find points that are enclosed in loop
# For that purpose, we will raycast from west to east, 
# for each point we count number of walls found
# if number is odd we are enclosed in the loop.

