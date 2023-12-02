import csv
import re

print("Welcome to day 2 of AoC 2023")

data = []

with open("data.csv", newline="\n") as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\n")
    for row in spamreader:
        try:
            # print(row[0])
            string = row[0]
            # print(string)
            string = string[5:]
            game = string.split(": ")
            results = game[1].split("; ")
            # print(results)
            data.append([game[0], results])
        except:
            data.append("")
            continue

result_1 = 0

for i in data:
    game_possible = True
    for x in i[1]:
        counts = x.split(", ")
        for y in counts:
            if "red" in y:
                number = [int(n) for n in y.split() if n.isdigit()]
                if number[0] > 12:
                    # print(f"Game {i[0]}: {y} game is not possible")
                    game_possible = False
                    continue
            if "green" in y:
                number = [int(n) for n in y.split() if n.isdigit()]
                if number[0] > 13:
                    # print(f"Game {i[0]}: {y} game is not possible")
                    game_possible = False
                    continue
            if "blue" in y:
                number = [int(n) for n in y.split() if n.isdigit()]
                if number[0] > 14:
                    # print(f"Game {i[0]}: {y} game is not possible")
                    game_possible = False
                    continue
    if game_possible:
        # print("game_possible")
        result_1 = result_1 + int(i[0])

print(f"The answer to the first puzzle is: {result_1}") #2006

################## PUZZLE 2 #######################

result_2 = 0

for i in data:
    red = 0
    green = 0
    blue = 0
    for x in i[1]:
        counts = x.split(", ")
        for y in counts:
            if "red" in y:
                number = [int(n) for n in y.split() if n.isdigit()]
                if number[0] > red:
                    red = number[0]
            if "green" in y:
                number = [int(n) for n in y.split() if n.isdigit()]
                if number[0] > green:
                    green = number[0]
            if "blue" in y:
                number = [int(n) for n in y.split() if n.isdigit()]
                if number[0] > blue:
                    blue = number[0]
    result_2 = result_2 + (red * green * blue)

print(f"The answer to the second puzzle is: {result_2}") #84911
