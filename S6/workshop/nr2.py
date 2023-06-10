"""
2.	Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go
Kotlin
Swift
"""

my_list = ['GO', 'Kotlin', 'Swift']


with open('hello.txt', 'a') as f:
    f.write('\n')
    for i in my_list:
        f.write(i + '\n')

with open('hello.txt', 'r') as f:
    lines = f.read()
    print(lines)
