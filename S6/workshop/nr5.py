"""
5.	Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
Read the file using Python’s `csv` standard library, and display it in the terminal as a table,
using the options for string formatting from Python:



id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu		21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa			29	9.0

"""

import csv

with open('students.csv', 'w', newline='') as csv_file:
    create_file = csv.writer(csv_file)
    create_file.writerow(['id', 'fname', 'lname', 'age', 'grade'])
    create_file.writerow(['1', 'Maria', 'Popescu', 31, 7.5])
    create_file.writerow(['2', 'Andrei', 'Ionescu', 26, 8.0])
    create_file.writerow(['3', 'Adriana', 'Marinescu', 21, 7.5])
    create_file.writerow(['4', 'Matei', 'Gheorghescu', 42, 8.5])
    create_file.writerow(['5', 'Eusebiu', 'Pop', 33, 9.5])
    create_file.writerow(['6', 'Ioana', 'Popa', 29, 9.0])

with open('students.csv', 'r') as csv_file:
    read_file = csv.reader(csv_file)
    header = next(read_file)
    print(header)
    print(f'{header[0]:4} {header[1]:13} {header[2]:15} {header[3]:5} {header[4]:5}')
    print('-' * 50)
    for row in read_file:
        # print(row)
        print(f'{row[0]:4} {row[1]:13} {row[2]:15} {row[3]:5} {row[4]:5}')
