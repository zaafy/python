from math import sqrt
f = open('words.txt')
words = f.read()
f.close()
words = words.strip().split(',')

def convert(character):
    return ord(character)-64

counter = 0

for word in words:
    x = sum(map(convert, word[1:-1]))
    if sqrt(8*x+1) == int(sqrt(8*x+1)):
        counter += 1

print(counter)