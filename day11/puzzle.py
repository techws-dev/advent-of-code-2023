# Open file, then translate into a list of lists
# Each tile of space_map can be accessed via space_map[y][x] (y and x starting at 0)
with open('puzzle-input.txt') as f:
    space_map = [*map(lambda l: [c for c in l if c != '\n'], f.readlines())]

# Generate expansion of the map
columns_with_galaxies = []
for y, line in reversed([*enumerate(space_map)]):
    if line == ['.'] * len(line):
        space_map.insert(y, line.copy())
    for x, tile in enumerate(line):
        if tile == '#' and x not in columns_with_galaxies:
            columns_with_galaxies += [x]

for x in reversed(range(len(space_map[0]))):
    if x not in columns_with_galaxies:
        for y, line in enumerate(space_map):
            space_map[y].insert(x, '.')

# Check map has been expanded
#print('\n'.join([''.join(x) for x in space_map]))

# Get list of galaxies (ordered from left to right, top to bottom)
galaxies = []
for y, line in enumerate(space_map):
    for x, tile in enumerate(line):
        if tile == '#':
            galaxies += [(x,y)]

# Check galaxies
#print(galaxies)

# Calculate shortest path of all pairs of galaxies
distances = 0
for i, galaxy_from in enumerate(galaxies[:-1]):
    for galaxy_to in galaxies[i+1:]:
        distances += abs(galaxy_from[0]-galaxy_to[0]) + abs(galaxy_from[1]-galaxy_to[1])

# Get result
print('Sum of distances between all galaxies:')
print(distances)