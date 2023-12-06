import re


# with open('input.txt', 'r') as file:
with open('input.txt', 'r') as file:
    data = file.readlines()

data = ' '.join([d.rstrip() for d in data])

map_types = [
    'seeds:',
    'seed-to-soil map:',
    'soil-to-fertilizer map:',
    'fertilizer-to-water map:',
    'water-to-light map:',
    'light-to-temperature map:',
    'temperature-to-humidity map:',
    'humidity-to-location map:'
]

mappings = []
for m in range(len(map_types)):
    if m != len(map_types)-1:
        x = re.findall('(?<='+map_types[m]+'\s).*?(?='+map_types[m+1]+')', data)
    else:
        x = re.findall('(?<='+map_types[m]+'\s).*', data)
    mappings.append(x[0].split())
mappings = [list(map(int, m)) for m in mappings]

result = [seed for seed in mappings[0]]
for i in range(1, len(mappings)):
# for i in [1]:
    dest = [mappings[i][k*3] for k in range(int(len(mappings[i])/3))]
    source = [mappings[i][k*3+1] for k in range(int(len(mappings[i])/3))]
    ranges = [mappings[i][k*3+2] for k in range(int(len(mappings[i])/3))]

    for j in range(len(result)):
        for k in range(len(source)):
            if source[k] <= result[j] < (source[k] + ranges[k]):
                result[j] = (result[j] - source[k]) + dest[k]
                break

print(min(result))
