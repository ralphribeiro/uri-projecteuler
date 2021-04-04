"""
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
"""


with open('ex22_names_scores.txt', 'rt') as file:
    names = [f.strip('"') for f in file.read().split(',')]

names.sort()

letter_value = {chr(v): lt for lt, v in enumerate(range(65, 91), 1)}

r = int()
for i, name in enumerate(names, 1):
    name_score = int()
    for letter in name:
        name_score += letter_value[letter]
    r += name_score * i

print(r)
