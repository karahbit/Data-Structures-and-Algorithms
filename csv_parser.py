# Approach 1: Using CSV module
import csv

print("Using CSV module:")
line = 'foo, bar, "one, two", three four'
print(line)

reader = csv.reader([line], skipinitialspace=True)
res = []
for r in reader:
    for i in r:
        res.append(i)
print(res)

# Construct the line back
# line = ", ".join(res)
line = ""
for i, string in enumerate(res):
    if "," in string:
        line += '"' + string + '"'
    else:
        line += string

    if i != len(res) - 1:
        line += ', '

print(line)


# Approach 2: Replacing all delimiters inside quotes, splitting and then replacing back
print("\nUsing replace and split:")
print(line)

in_quote = None
indexes = []
for i, letter in enumerate(line):
    if in_quote:
        if (letter == in_quote):
            in_quote = None
        else:
            if letter == ',':
                indexes.append(i)
    else:
        if (letter == '"' or letter == "'"):
            in_quote = letter
for i in indexes:
    line = line[:i] + ';' + line[i+1:]
print(line)

res = line.split(', ')
print(res)

for i, string in enumerate(res):
    if ';' in string:
        string = string.replace(';', ',')
        res[i] = string.strip('"')
print(res)

# Construct the line back
line = ""
for i, string in enumerate(res):
    if "," in string:
        line += '"' + string + '"'
    else:
        line += string

    if i != len(res) - 1:
        line += ', '
print(line)

# Approach 3: Using loops and conditionals
print("\nUsing loops and conditionals:")
print(line)


def comma_split(string):
    last = 0
    splits = []
    in_quote = None
    for i, letter in enumerate(string):
        if in_quote:
            if (letter == in_quote):
                in_quote = None
        else:
            if (letter == '"' or letter == "'"):
                in_quote = letter

        if not in_quote and letter == ',':
            splits.append(string[last:i].strip(' "'))
            last = i+1

    if last < len(string):
        splits.append(string[last:].strip(' "'))

    return splits


res = comma_split(line)
print(res)

# Construct the line back
# line = ", ".join(res)
line = ""
for i, string in enumerate(res):
    if "," in string:
        line += '"' + string + '"'
    else:
        line += string

    if i != len(res) - 1:
        line += ', '
print(line)
