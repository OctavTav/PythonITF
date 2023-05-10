l = list([1, 5, 100])

my_iterator = iter(l)       # creez un iterator
print(next(my_iterator))    # va printa 1
print(next(my_iterator))    # va printa 5
print(next(my_iterator))    # va printa 100
# print(next(my_iterator))    # va atunca excepta StopIteration

"""
Orice clasa care implementeaza cele 2 metode metionate devine automat iterabila.
Astfel, putm sa ne construim proprii iteratori la nevoie.
Pe langa folosirea lui next, putem 
"""


class AlphabetIretator:

    def __iter__(self):
        self.letter = 'A'
        return self

    def __next__(self):
        current_letter = self.letter
        if current_letter == 'D':
            raise StopIteration
        self.letter = chr(ord(self.letter) + 1) #folosim ord ca sa aflam codul in unicod ca sa putem adauga 1
        return current_letter

a1 = AlphabetIretator()
alpha_iter = iter(AlphabetIretator())
# print(next(alpha_iter))
# print(next(alpha_iter))
# print(next(alpha_iter))

for letter in alpha_iter:
    print(letter)



