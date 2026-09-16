fruits = ("apple", "banana", "orange")
fruits_list = list(fruits)
fruits_list.append("grape")
fruits = tuple(fruits_list)
print(fruits)
brothers = ("omar", "zaid")
sisters = ("nadia", "bilksi")
siblings = brothers + sisters
print(siblings)
print("I have", len(siblings), "siblings")
siblings_list = list(siblings)
siblings_list.append("rafiq ahmad lone , muneera ")
family = tuple(siblings_list)
print(f"our family consists of these people\n{family}")
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
is_estonia_nordic = "Estonia" in nordic_countries
is_iceland_nordic = "Iceland" in nordic_countries
print("is estonia a nordic country", is_estonia_nordic)
print("is iceland a nordic country", is_iceland_nordic)
print(nordic_countries[:3])
print(nordic_countries[-2::])
bro_1, bro_2 = brothers
print("my first brother is:", bro_1)
