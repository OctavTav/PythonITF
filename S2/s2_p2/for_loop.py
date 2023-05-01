matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for elem in row:
        print(elem)

print('-' * 80)
for x in range(5):
    for y in range(5):
        print(f'{x} X {y} = {x * y}')
    print()