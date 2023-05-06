# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

# 10. Dorel a făcut contestație și a primit 6
# ●	Modifică nota lui Dorel în 6
# ●	Printează nota după modificare

# 11. Gigel se transferă din clasă
# ●	Căuta o funcție care să îl șteargă
# ●	Vine un coleg nou. Adaugă Ionică, cu nota 9
# ●	Printează noii elevi

dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}

print(dict1.keys())
for i in dict1.keys():
    print(i)
print('-' * 50)

for elev, nota in dict1.items():
    print(f"{elev} a luat nota {nota}")
print('-' * 50)

dict1['Dorel'] = 6
print(f"Nota lui Dorel a fost modificata si acum este {dict1['Dorel']}")
print('-' * 50)

print("Gigel s-a transferat si a venit un coleg nou")
dict1.pop('Dorel')
dict1['Ionica'] = 9
# dict1_update({'Ionica': 9})
print("Lista noua de elevi:")
for elev in dict1.keys():
    print({elev}, end=" ")
