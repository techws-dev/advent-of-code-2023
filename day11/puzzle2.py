# Open file, then translate into a list of lists
# Each tile of space_map can be accessed via space_map[y][x] (y and x starting at 0)
with open('puzzle-input.txt') as f:
    space_map = [*map(lambda l: [c for c in l if c != '\n'], f.readlines())]

# Solution will be the same here, except we will not expand the map
# Just get indexes of lines and rows with expansion
rows_expanded = []
columns_with_galaxies = []
for y, line in enumerate(space_map):
    if line == ['.'] * len(line):
        rows_expanded += [y]
    for x, tile in enumerate(line):
        if tile == '#' and x not in columns_with_galaxies:
            columns_with_galaxies += [x]

cols_expanded = []
for x in range(len(space_map[0])):
    if x not in columns_with_galaxies:
        cols_expanded += [x]

# Check expansions
#print('rows expanded:')
#print(rows_expanded)
#print('cols expanded:')
#print(cols_expanded)

# Get list of galaxies (ordered from left to right, top to bottom)
galaxies = []
for y, line in enumerate(space_map):
    for x, tile in enumerate(line):
        if tile == '#':
            galaxies += [(x,y)]

# Check galaxies
#print(galaxies)

# Calculate shortest path of all pairs of galaxies
# Now if we get in a space expanded, we multiply by 1 000 000
distances = 0
for i, galaxy_from in enumerate(galaxies[:-1]):
    for galaxy_to in galaxies[i+1:]:
        distance = 0

        # We have to order the loop before
        from_x = min(galaxy_from[0], galaxy_to[0])
        to_x = max(galaxy_from[0], galaxy_to[0])
        from_y = min(galaxy_from[1], galaxy_to[1])
        to_y = max(galaxy_from[1], galaxy_to[1])

        for x in range(from_x, to_x):
            if x in cols_expanded:
                distance += 1000000
            else:
                distance += 1
        for y in range(from_y, to_y):
            if y in rows_expanded:
                distance += 1000000
            else:
                distance += 1
        distances += distance

# Get result
print('Sum of distances between all galaxies:')
print(distances)