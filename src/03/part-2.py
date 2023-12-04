import re
from pathlib import Path


def is_gear(char):
    regexp = r'[*]'
    return bool(re.search(regexp, char))


def is_number(char):
    regexp = r'[\d]'
    return bool(re.search(regexp, char))


def index_numbers(x, k):
    search_list = [
        (k[0], k[1]+1),
        (k[0]+1, k[1]+1),
        (k[0]+1, k[1]),
        (k[0]+1, k[1]-1),
        (k[0], k[1]-1),
        (k[0]-1, k[1]-1),
        (k[0]-1, k[1]),
        (k[0]-1, k[1]+1)
    ]
    match = [is_number(x[l[0]][l[1]]) for l in search_list]
    return [a for a, b in zip(search_list, match) if b]


def find_number(x, k):
    j_start = k[1]
    while is_number(x[k[0]][j_start-1]):
        j_start -= 1
    j = j_start
    number = []
    while is_number(x[k[0]][j]):
        number.append(x[k[0]][j])
        if j != 139:
            j += 1
        else:
            return ''.join(number)
    return ''.join(number)


def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    x = [list(data[i].strip()) for i in range(len(data))]

    ind = [(i, j) for i in range(len(x)) for j in range(len(x)) if is_gear(x[i][j])]

    result = 0
    values = []
    for k in ind:
        match = index_numbers(x, k)
        for m in match:
            values.append(find_number(x, m))
        if len(list(set(values))) == 2:
            result += int(list(set(values))[0])*int(list(set(values))[1])
        values = []


if __name__ == "__main__":
    main()
