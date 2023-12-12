# Open file, then translate into a list of lists
with open('puzzle-input.txt') as f:
    springs_list = [*map(lambda l: l.replace('\n', '').split(' '), f.readlines())]

# Brute force solution, will probably not work on puzzle 2...
def check_springs(s, test):
    check = ','.join(map(lambda y: str(len(y)),[x for x in s.split('.') if x.count('#')>0]))
    return check == test

arrangements = 0
for springs,test in springs_list:
    unknow = springs.count('?')
    for i in range(2**unknow):
        filter = format(i, '0{}b'.format(unknow))
        s = springs
        for f in filter:
            s = s.replace('?', '#' if f=='1' else '.', 1)
        if check_springs(s, test) == True:
            arrangements += 1

print('Arrangements found:')
print(arrangements)