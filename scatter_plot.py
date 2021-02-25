import itertools

iterable = ["Birthday",
"Best Hand",
"Arithmancy",
"Astronomy",
"Herbology",
"Defense Against the Dark Arts",
"Divination",
"Muggle Studies",
"Ancient Runes",
"History of Magic",
"Transfiguration",
"Potions",
"Care of Magical Creatures",
"Charms",
"Flying",
"Year",
"Month",
"Day"]

allIterables = list(itertools.combinations(iterable, 2))
for el in wow:
    print(el)