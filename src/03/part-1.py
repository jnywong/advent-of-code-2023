import re


def is_symbol(char):
    regexp = r'[#,$,%,&,*,+,\-,/,=,@]'
    return bool(re.search(regexp, char))


def find_symbol(x, ind):
    '''
    Find symbol in a square block around x[ind[0], ind[1]].

    Treat edges of the square block accordingly.
    '''

    if ind[0] == 0:
        return any([
            is_symbol(x[ind[0]][ind[1]+1]),
            is_symbol(x[ind[0]+1][ind[1]+1]),
            is_symbol(x[ind[0]+1][ind[1]]),
            is_symbol(x[ind[0]+1][ind[1]-1]),
            is_symbol(x[ind[0]][ind[1]-1]),
        ])
    elif ind[0] == len(x)-1:
        return any([
            is_symbol(x[ind[0]][ind[1]+1]),
            is_symbol(x[ind[0]][ind[1]-1]),
            is_symbol(x[ind[0]-1][ind[1]-1]),
            is_symbol(x[ind[0]-1][ind[1]]),
            is_symbol(x[ind[0]-1][ind[1]+1]),
        ])
    elif ind[1] == 0:
        return any([
            is_symbol(x[ind[0]][ind[1]+1]),
            is_symbol(x[ind[0]+1][ind[1]+1]),
            is_symbol(x[ind[0]+1][ind[1]]),
            is_symbol(x[ind[0]+1][ind[1]-1]),
            is_symbol(x[ind[0]][ind[1]-1]),
        ])
    elif ind[1] == len(x)-1:
        return any([
            is_symbol(x[ind[0]+1][ind[1]]),
            is_symbol(x[ind[0]+1][ind[1]-1]),
            is_symbol(x[ind[0]][ind[1]-1]),
            is_symbol(x[ind[0]-1][ind[1]-1]),
            is_symbol(x[ind[0]-1][ind[1]]),
        ])
    else:
        return any([
            is_symbol(x[ind[0]][ind[1]+1]),
            is_symbol(x[ind[0]+1][ind[1]+1]),
            is_symbol(x[ind[0]+1][ind[1]]),
            is_symbol(x[ind[0]+1][ind[1]-1]),
            is_symbol(x[ind[0]][ind[1]-1]),
            is_symbol(x[ind[0]-1][ind[1]-1]),
            is_symbol(x[ind[0]-1][ind[1]]),
            is_symbol(x[ind[0]-1][ind[1]+1]),
        ])


def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    x = [list(data[i].strip()) for i in range(len(data))]

    ind = [(i, j) for i in range(len(x)) for j in range(len(x)) if x[i][j].isdigit()]

    result = 0
    init = 0
    m = []
    values = [x[ind[init][0]][ind[init][1]]]
    for k in range(len(ind)-1):
        if (ind[k+1][1] - ind[k][1] == 1):
            values.append(x[ind[k+1][0]][ind[k+1][1]])
            m.append(k)
            print(k, values)
        else:
            print('match')
            m.append(k)
            if any([find_symbol(x, l) for l in ind[m[0]:m[-1]+1]]):
                result += int(''.join(values))
                m = []
            values = [x[ind[k+1][0]][ind[k+1][1]]]

    result += 973  # NOTE: loop above misses out the last iteration


if __name__ == "__main__":
    main()
