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


def max_cubes(n_red, n_blue, n_green):
    max_red = max(n_red)
    max_blue = max(n_blue)
    max_green = max(n_green)
    return max_red, max_blue, max_green


def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    power = []
    for i in range(len(data)):
        game_id, n_red, n_blue, n_green = parse_games(data[i])
        max_red, max_blue, max_green = max_cubes(n_red, n_blue, n_green)
        power.append(max_red*max_blue*max_green)
    print(sum(power))


if __name__ == "__main__":
    main()
