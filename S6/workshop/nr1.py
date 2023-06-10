"""
1.	Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js
"""

with open('hello.txt') as f:
    lines = f.read()
    print(lines)
