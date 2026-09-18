# count = 0
# while count <= 10:
#     print(count)
#     count += 1
# for i in range(11):
#     print(i)
# count = 10
# while count >= 0:
#     print(count)
#     count -= 1
# for i in range(10, -1, -1):
#     print(i)
# for i in range(7):
#     print("#" * i)
# for i in range(0, 7, 1):
#     print("*" * i)
# for i in range(10, -1, -1):
#     print("#" * i)
# for i in range(11):
#     print(f"{i} x {i} = {i * i}")
# skills = ["Python", "Numpy", "Pandas", "Django", "Flask"]
# for item in skills:
#     print(item)
# for item in skills[2:5:1]:
#     print(item)
# for i in range(2, 101, 2):
#     print(i)
# for i in range(1, 100):
#     if i % 2 != 0:
#         print(i)
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total} ")
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(
    f"the sum of all even numbers is {even_sum} and the sum of all odd numbers is {odd_sum}"
)
fruits = ["banana", "orange", "mango", "lemon"]
reserved_fruits = []
for item in fruits:
    reserved_fruits.insert(0, item)
print(reserved_fruits)
countries = [
    "Afghanistan",
    "Finland",
    "Albania",
    "Algeria",
    "Iceland",
    "Germany",
    "IreLand",
    "Brazil",
    "Poland",
    "Japan",
    "Switzerland",
    "Thailand",
    "Canada",
    "New Zealand",
    "Netherlands",
]
land_countries = []
for item in countries:
    if "land" in item.lower():
        land_countries.append(item)
print(
    f"The number of countries that has 'land'in them are {len(land_countries)} and those are:\n{land_countries}"
)
