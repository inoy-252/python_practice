from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]


def to_upper(country):
    return country.upper()


upper_countries = list(map(to_upper, countries))
print(upper_countries)

upper_countries = list(map(lambda c: c.upper(), countries))
print(upper_countries)

squared_numbers = list(map(lambda n: n**2, numbers))
print(squared_numbers)

land_countries = list(filter(lambda c: "land" in c, countries))
print(land_countries)

countries_wrd_6 = list(filter(lambda c: len(c) == 6, countries))
countries_wrd_more_6 = list(filter(lambda c: len(c) >= 6, countries))
countries_strt_e = list(filter(lambda c: c[0] == "E", countries))
print(countries_wrd_6)
print(countries_wrd_more_6)
print(countries_strt_e)

total_sum = reduce(lambda acc, cur: acc + cur, numbers)
print(total_sum)
total_product = reduce(lambda acc, cur: acc * cur, numbers)
print(total_product)
land_upper = list(map(lambda c: c.upper(), filter(lambda c: "land" in c, countries)))
print(land_upper)


def make_power(power):
    def calculate(base):
        return base**power

    return calculate


square = make_power(2)
cube = make_power(3)

print(square(5))
print(cube(6))


def banner_decorator(func):
    def wrapper():
        result = func()
        return f"{'=' * 40}\n{result.upper()}\n{'=' * 40}"

    return wrapper


@banner_decorator
def get_message():
    return "welcome to advanced python"


print(get_message())
