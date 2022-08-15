import sys
import math

text = input()
counter = 0
text_output = ''
n = 0
line = 0
cnt = 0
tmp = ''
tmp2 = ''
text += ' '

def add(counter, str_i):
    str_o = ''
    for item in range(counter):
        str_o += str_i
    return str_o

for item in text:
    if line == 1:
        if item == 'l':
            text_output += '\n'
            line = 0
            continue
        else:
            text_output += add(counter, 'n')
    if item == ' ':
        if tmp2:
            if ord(tmp2)<58 and ord(tmp2)>47:
                text_output += add(tmp1, tmp2)
                tmp2 = ''
        cnt = 0
        counter = 0
        continue
    if cnt == 1:
        if ord(item)<58 and ord(item)>47:
            tmp1 = counter
            tmp2 = item
            counter = int(str(counter)+item)
            continue
    if ord(item)<58 and ord(item)>47:
        counter = int(item)
        cnt = 1
        continue
    if item == 'n':
        line = 1
        continue
    if n == 1:
        if item == 'p':
            text_output += add(counter, ' ')
            n=0
            continue
        elif item == 'Q':
            text_output += add(counter, "'")
            n=0
            continue
        elif item == 'S':
            text_output += add(counter, chr(92))
            n=0
            continue
        elif item == 'l':
            text_output += add(counter, '\n')
            n=0
            continue
        else:
            text_output += add(counter, tmp)
            n=0
            continue
    if item == 's':
        tmp = item
        n=1
        continue
    if item == 'b':
        tmp = item
        n=1
        continue
    if counter:
        text_output += add(counter, item)
        continue

print(text_output)
