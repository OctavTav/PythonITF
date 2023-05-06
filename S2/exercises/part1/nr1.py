#1. Declară o listă note_muzicale în care să pui do re mi etc până la do
#●	Afișeaz-o.
#●	Inversează ordinea folosind slicing și suprascrie această listă.
#●	Printează varianta actuală (inversată).
#●	Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
#●	Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

note_muzicale = ['do', 're', 'mi', 'fa', 'so', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)

note_inversate = []
for i in range(len(note_muzicale)-1, -1, -1 ):
    note_inversate.append(note_muzicale[i])
#print(note_inversate)        # verific noua lista
note_muzicale = note_inversate
print(note_muzicale)