#3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
#   Găsește 2 variante să le unești într-o singură listă.

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]

list_combined_1 = list_1 + list_2

print(list_combined_1)
list_combined_2 = []

for i in list_1:
    list_combined_2.append(i)
for i in list_2:
    list_combined_2.append(i)

print(list_combined_2)