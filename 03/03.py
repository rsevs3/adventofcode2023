import csv
import re

print("Welcome to day 2 of AoC 2023")

data = []

with open("data.csv", newline="\n") as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\n")
    for row in spamreader:
        try:
            data.append(row[0])
        except:
            continue

def get_symbol_locations(row):
    locations = []
    if row == 0:
        for match in re.finditer("(\*)|(-)|(#)|(@)|(&)|(\/)|(\$)|(\+)|(=)|(%)", data[row]):
            locations.append(match.span()[0])
        for match in re.finditer("(\*)|(-)|(#)|(@)|(&)|(\/)|(\$)|(\+)|(=)|(%)", data[row+1]):
            locations.append(match.span()[0])
        return locations
    elif row == (len(data)-1):
        for match in re.finditer("(\*)|(-)|(#)|(@)|(&)|(\/)|(\$)|(\+)|(=)|(%)", data[(row-1)]):
            locations.append(match.span()[0])
        for match in re.finditer("(\*)|(-)|(#)|(@)|(&)|(\/)|(\$)|(\+)|(=)|(%)", data[row]):
            locations.append(match.span()[0])
        return locations
    else:
        for match in re.finditer("(\*)|(-)|(#)|(@)|(&)|(\/)|(\$)|(\+)|(=)|(%)", data[(row-1)]):
            locations.append(match.span()[0])
        for match in re.finditer("(\*)|(-)|(#)|(@)|(&)|(\/)|(\$)|(\+)|(=)|(%)", data[row]):
            locations.append(match.span()[0])
        for match in re.finditer("(\*)|(-)|(#)|(@)|(&)|(\/)|(\$)|(\+)|(=)|(%)", data[(row+1)]):
            locations.append(match.span()[0])
        return locations

result_1 = 0
row = 0

for i in data:
    symbols = get_symbol_locations(row)
    row = row + 1
    for match in re.finditer("[0-9]+", i):
        for x in symbols:
            if (x >= max(match.span()[0]-1,0)) and (x <= match.span()[1]):
                result_1 = result_1 + int(match.group())

print(f"The answer to the first puzzle is: {result_1}")
# 533775 is the answer

def get_star_locations(row):
    locations = []
    for match in re.finditer("(\*)", data[row]):
        locations.append(match.span()[0])
    return locations

result_2 = 0
row = 0

for i in data:
    stars = get_star_locations(row)
    row = row + 1
    match_1 = []
    match_2 = []
    loop = 0
    # print(stars)

    # Find any that are side by side
    for match_2 in re.finditer("[0-9]+", i):
        if loop == 0:
            match_1 = match_2
            loop = loop + 1
            continue
        for x in stars:
            if match_2.span()[0]-1 == x and match_1.span()[1] == x:
                # print(f"we have a side by side match at row {row}: {match_2}")
                result_2 = result_2 + (int(match_1.group()) * int(match_2.group()))
        match_1 = match_2

    # Find any that are side by side with a dot and star above/below

    if row < 2:
        continue
    else:
        for match in re.finditer("[0-9]+(\.)[0-9]+", i):
            # print(f"found a space separator at row: {row}")
            stars_above = get_star_locations(row-2)
            stars_below = get_star_locations(row)
            first_numer = match.group().split(".")
            # print(first_numer)
            for match_first in re.finditer("("+first_numer[0]+")", i):
                if (int(match_first.span()[1]) in stars_below) or (int(match_first.span()[1]) in stars_above):
                    # print(f"hit a star above or below at row {row}: {match_first}")
                    result_2 = result_2 + (int(first_numer[0]) * int(first_numer[1]))

    # Find any that adjacent to the side and below

    for match_side in re.finditer("[0-9]+", i):
        for x in stars:
            if (x == max(match_side.span()[0]-1, 0)) or (x == match_side.span()[1]):
                # print(f"one touching the side: {match_side}")
                for match_bottom in re.finditer("[0-9]+", data[row]):
                    if (x >= max(match_bottom.span()[0]-1,0)) and ( x <= match_bottom.span()[1]):
                        # print(f"we have a side adjacent below match: {match_bottom}")
                        result_2 = result_2 + (int(match_bottom.group()) * int(match_side.group()))

    # Find any that adjacent to the side and above

    if row < 2:
        # print(f"row is less than 2: {row}")
        continue
    else:
        for match_side in re.finditer("[0-9]+", i):
            for x in stars:
                if (x == max(match_side.span()[0]-1, 0)) or (x == match_side.span()[1]):
                    # print(f"one touching the side: {match_side}")
                    for match_above in re.finditer("[0-9]+", data[row-2]):
                        if (x >= max(match_above.span()[0]-1,0)) and ( x <= match_above.span()[1]):
                            # print(f"we have a side adjacent above match at row {row}: {match_above}")
                            result_2 = result_2 + (int(match_above.group()) * int(match_side.group()))

    # Find any that are adjacent above and below
    if row == len(data)-1:
        print("continue")
        break
    else:
        print(row)
        stars = get_star_locations(row)
        # print(stars)
        for match_top in re.finditer("[0-9]+", i):
            for x in stars:
                if (x >= max(match_top.span()[0]-1,0)) and ( x <= match_top.span()[1]):
                    # print(f"we have a touch below: {match_top}")
                    for match_bottom in re.finditer("[0-9]+", data[row+1]):
                        if (x >= max(match_bottom.span()[0]-1,0)) and ( x <= match_bottom.span()[1]):
                            print(f"we have an above below match at row {row}: {match_bottom}")
                            result_2 = result_2 + (int(match_bottom.group()) * int(match_top.group()))

print(result_2)
#60986853 too low
# 66706388 too low
# 115552183 too high
# 72482995 nope
# 76737976 nope





