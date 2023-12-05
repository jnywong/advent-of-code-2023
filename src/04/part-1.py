import re


def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    result = 0
    for d in data:
        numbers = re.findall('(\d+)', d)
        win_num = numbers[1:11]
        my_num = numbers[11:]
        matches = [win_num.count(x) for x in my_num]
        if sum(matches) != 0:
            result += 2**(sum(matches)-1)


if __name__ == "__main__":
    main()
