import csv
import re

print("Welcome to day 1 of AoC 2023")

data = []

with open("data.csv", newline="\n") as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\n")
    for row in spamreader:
        try:
            # print(row[0])
            data.append(row[0])
        except:
            data.append("")
            continue

sum = 0

for i in data:
    first = re.search("([0-9])", i)
    last = re.search("([0-9])", i[::-1])
    combined = first.group(1) + last.group(1)
    sum = sum + int(combined)

print(f"The answer to the first puzzle is: {sum}")


################## PUZZLE 2 #######################


def word_to_character(word):
    match word:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"

sum = 0

for i in data:
    first = re.search("([0-9]|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))", i)
    last = re.search("(?s:.*)([0-9]|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))", i)

    if not first.group(1).isnumeric():
        first = word_to_character(first.group(1))
    else:
        first = first.group(1)

    if not last.group(1).isnumeric():
        last = word_to_character(last.group(1))
    else:
        last = last.group(1)

    combined = first + last
    sum = sum + int(combined)

print(f"The answer to the second puzzle is: {sum}")
