import re


def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    n_cards = [1]*len(data)
    for k in range(len(data)):
        numbers = re.findall('(\d+)', data[k])
        win_num = numbers[1:11]
        my_num = numbers[11:]
        matches = [win_num.count(x) for x in my_num]
        for j in range(sum(matches)):
            n_cards[k+j+1] += n_cards[k]
    print(sum(n_cards))

if __name__ == "__main__":
    main()
