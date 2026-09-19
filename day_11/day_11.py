# a = float(input("Enter a number: "))
# b = float(input("Enter the second number: "))


# def add_two_numbers(a, b):
#     result = a + b
#     return result


# print(f"the sum of {a} and {b} is {add_two_numbers(a, b)}")

# r = float(input("Enter the radius of your circle: "))


# def area_of_circle(r):
#     area = 3.14 * (r) ** 2
#     return area


# print(f"The area of your circle with radius {r} is {area_of_circle(r):.2f}")
# celcius = float(input("enter the temperature that you want to be converted: "))


# def convert_celsius_to_fahrenheit(celcius):
#     fahrenheit = (celcius * (9 / 5)) + 32
#     return fahrenheit


# print(
#     f"{celcius} degree celcius is equal to {convert_celsius_to_fahrenheit(celcius):.1f} degree fahrenheit"
# )
# current_month = input("enter the current month: ")


# def check_season(current_month):
#     clean_month = current_month.capitalize()
#     if clean_month in ["December", "January", "February"]:
#         return "Winter"
#     elif clean_month in ["March", "April", "May"]:
#         return "Spring"
#     elif clean_month in ["June", "July", "August"]:
#         return "Summer"
#     elif clean_month in ["September", "October", "November"]:
#         return "Autumn"
#     else:
#         return "(unknown/invalid month entered)"


# print(
#     f"Based on the month you entered the current season is {check_season(current_month)}"
# )


# def reverse_list(lst):
#     reversed_items = []
#     for item in lst:
#         reversed_items.insert(0, item)
#     return reversed_items


# fruits = ["banana", "apple", "orange", "mango", "lemon"]
# print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list(fruits))


# mass = float(input("what is the mass of object: "))
# grav_input = input("Enter custom gravity (or just press Enter for Earth): ")


# def calculate_weight(mass, gravity=9.81):
#     weight = mass * gravity
#     return weight


# if grav_input == "":
#     print(f"weight is equal to {calculate_weight(mass)}")
# else:
#     print(f"weight is equal to {calculate_weight(mass, float(grav_input)):.2f} ")


user_text = input("enter the numbers you want to add seperated by spaces: ")
words = user_text.split()
clean_nums = []
for w in words:
    clean_nums.append(float(w))


def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


result = add_all_nums(*clean_nums)

print(add_all_nums(1, 2, 34, 34))
print(f"sum of all the numbers given is: {result}")
