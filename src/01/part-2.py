import re


def word2num(line):
    words = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
        'ten': 't10n',
    }
    search = [(i, j) for j in words.keys()
              for i in [m.start()
                        for m in re.finditer('(?='+j+')', line)]]
    try:
        i_min = min(search, key=lambda t: t[0])
        line = line.replace(i_min[1], words[i_min[1]])
    except ValueError:
        pass
    try:
        i_max = max(search, key=lambda t: t[0])
        line = line.replace(i_max[1], words[i_max[1]])
    except ValueError:
        pass
    return line


def main():
    with open("input.txt", "r") as file:
        values = []
        for line in file:
            line = word2num(line)
            values.append(''.join(x for x in line if x.isdigit()))

    calibration = [f"{v[0]}{v[-1]}" for v in values]
    with open("output.txt", "w") as file:
        for k in range(len(calibration)):
            file.write(f"{calibration[k]}\n")
    result = sum(list(map(int, calibration)))
    print(result)


if __name__ == "__main__":
    main()
