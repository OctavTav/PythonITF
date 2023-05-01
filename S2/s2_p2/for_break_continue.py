numbers = [1, 4, -5, 10 ,12, 100, 0, 1, 23, 27]
for number in numbers:
    if number <0:
        print(f'Am gasit un numar negativ: {number}')
        break
    else:
        print(f'Nu am gasit inca numar negativ, mai cautam...')
else:
    print(f'Nu am gasit nici un numar negativ')