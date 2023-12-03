import re


def parse_games(game):
    game_id = int(re.findall("[^Game\s](?:\d*)(?=:)", game)[0])
    n_red = list(map(int, [re.sub("\sred", "", x) 
                           for x in re.findall("\d+\sred", game)]))
    n_blue = list(map(int, [re.sub("\sblue", "", x)
                            for x in re.findall("\d+\sblue", game)]))
    n_green = list(map(int, [re.sub("\sgreen", "", x)
                             for x in re.findall("\d+\sgreen", game)]))
    return game_id, n_red, n_blue, n_green


def check_possible(n_red, n_blue, n_green):
    nmax_red = 12
    nmax_green = 13
    nmax_blue = 14
    if (all(r <= nmax_red for r in n_red) and
            all(b <= nmax_blue for b in n_blue) and
            all(g <= nmax_green for g in n_green)):
        return True
    else:
        return False


def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    possible_id = []
    for i in range(len(data)):
        game_id, n_red, n_blue, n_green = parse_games(data[i])
        if check_possible(n_red, n_blue, n_green):
            possible_id.append(game_id)
    print(sum(possible_id))


if __name__ == "__main__":
    main()
