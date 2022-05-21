import re

def simplify(string):
    string = re.sub('\s{2,}', ' ', (string + ' ').replace("''", '').replace("2'", '2').replace('(', '').replace(')', '').replace('\n', ' '))

    prev_string = ''
    while prev_string != string:
        prev_string = string
        for i in ('B', 'D', 'F', 'L', 'R', 'U'):
            for pair in [(f"{i} {i} ", f"{i}2 "), (f"{i} {i}' ", ''), (f"{i} {i}2 ", f"{i}' "), (f"{i}' {i} ", ''), (f"{i}' {i}' ", f"{i}2 "), (f"{i}' {i}2 ", f"{i} "), (f"{i}2 {i} ", f"{i}' "), (f"{i}2 {i}' ", f"{i} "), (f"{i}2 {i}2 ", '')]:
                string = string.replace(*pair)

    return string.strip(' ')

def reverse(string):
    return simplify(' '.join([char + "'" if char != '' else '' for char in string.split(' ')][::-1]))
