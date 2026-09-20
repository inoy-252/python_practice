import random
import string

print("All lowercase letters:", string.ascii_lowercase)
# print("All digits", string.digits)


# char_pool = string.ascii_lowercase + string.digits
# lucky_char = random.choice(char_pool)
# print("Random pick:", lucky_char)


# def random_user_id():

#     user_id = ""
#     for _ in range(6):
#         user_id += random.choice(char_pool)
#     return user_id


# print("Your generated ID: ", random_user_id())


# def user_id_gen_by_user():
#     num_chars = int(input("Number of characters: "))
#     num_ids = int(input("Number of IDs: "))
#     for _ in range(num_ids):
#         user_id = ""
#         for _ in range(num_chars):
#             user_id += random.choice(char_pool)
#         print(user_id)


# user_id_gen_by_user()


def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},  {g},  {b})"


# print(rgb_color_gen())


def list_of_hexa_colors(num):
    hex_chars = "0123456789abcdef"
    colors = []
    for _ in range(num):
        single_color = "#"
        for _ in range(6):
            single_color += random.choice(hex_chars)
        colors.append(single_color)
    return colors


# num = int(input("how many hexa colors are needed? "))
# print(list_of_hexa_colors(num))


def list_of_rgb_colors(num):
    colors = []
    for _ in range(num):
        colors.append(rgb_color_gen())
    return colors


print(list_of_rgb_colors(4))


def generate_colors(color_type, num):
    if color_type == "hexa":
        return list_of_hexa_colors(num)
    elif color_type == "rgb":
        return list_of_rgb_colors(num)
    else:
        return "Invalid color type! Please choose 'hexa' or 'rgb'."


print(generate_colors("hexa", 3))
print(generate_colors("rgb", 2))


def shuffle_list(lst):
    copied_list = lst.copy()
    random.shuffle(copied_list)
    return copied_list


print(shuffle_list([1, 2, 3, 4, 5, "inoy", "yasir", "Imran", "anees", "mehran"]))


def seven_unique_numb():
    return random.sample(range(10), 7)


print(seven_unique_numb())
