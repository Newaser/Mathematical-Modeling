filepath = "data.txt"

f = open(filepath, 'r')
print('    ' + f.read().replace('\t', ',\t').replace('\n', '\n    '))
