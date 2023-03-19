field = [[None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None, None]]

num_rows = len(field)
num_columns = len(field[0])

for column in range(num_columns):
    print('+----', end='')
print('+')

for row in range(num_rows):
    for column in field[row]:
        print("|    ", end='')
    print('|')
    for column in field[row]:
        print("|    ", end='')
    print('|')
    for column in range(num_columns):
        print('+----', end='')
    print('+')