"""
3.	Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
"""

# with open('hello.txt', 'r') as f:
#     lines = [line.rstrip() for line in f]
#     print(lines)
#     odd_lines = []
#     for i in range(0, len(lines)):
#         if i % 2 == 0:
#             odd_lines.append(lines[i])
#     print(odd_lines)

with open('hello.txt', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):
        print(lines[i])
