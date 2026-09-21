numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_num = [x for x in numbers if x <= 0]
print(neg_num)
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [number for outer in list_of_lists for middle in outer for number in middle]
print(flattened)

table = []
for i in range(11):
    table.append((i, 1, i, i**2, i**3, i**4, i**5))
print(table)

table_comp = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(table_comp)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
formatted_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for sub in countries
    for country, city in sub
]
print(formatted_countries)


formatted_countries = [
    {"country": country.upper(), "city": city.upper()}
    for sub in countries
    for country, city in sub
]
print(formatted_countries)

names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]

full_names = [f"{first} {last}" for sub in names for first, last in sub]
print(full_names)

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print("Slope:", slope(1, 2, 3, 6))
