import re

sentence = (
    "I bought 3 apples for 15 dollars and 2 oranges for 8 dollars in the year 2026."
)

numbers = re.findall(r"\d+", sentence)
print("Extracted Numbers: ", numbers)


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

numbers_2 = re.findall(r"-?\d+", text)
points = [int(n) for n in numbers_2]

distance = max(points) - min(points)
print("The distance between the furthest particles is: ", distance)


dirty_text = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple."

clean_text = re.sub(r"[^a-zA-Z\s]", "", dirty_text)

print(dirty_text)
print(clean_text)

words = clean_text.split()
word_count = {w: words.count(w) for w in set(words)}
most_frequent = max(word_count, key=word_count.get)
print(
    f" Most frequent word: '{most_frequent}' (appears {word_count[most_frequent]} times)"
)


def is_valid_variable(name):
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(pattern, name))


test_names = [
    "first_name",
    "first-name",
    "1first_name",
    "firstname",
    "_secret_key",
    "total$",
]
for name in test_names:
    print(f"{name:15} -> {is_valid_variable(name)}")
