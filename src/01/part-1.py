with open("input.txt", "r") as file:
    values = []
    for line in file:
        values.append(''.join(x for x in line if x.isdigit()))

calibration = [f"{v[0]}{v[-1]}" for v in values]
result = sum(list(map(int, calibration)))
print(result)
