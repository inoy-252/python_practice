# age = int(input("what is your age? "))
# if age >= 18:
#     print("you are old enough to get a driving licence")
# else:
#     print(f"you need {18 - age} years to become eligible for a driving licence")
# age_1 = int(input("what your age Emran ?"))
# age_2 = int(input("whats's your age Yasir? "))
# if age_1 < age_2:
#     print(f"Emran you are {age_2 - age_1} years younger than me ")
# elif age_1 > age_2:
#     print(f"Emran you are {age_1 - age_2} years older than me ")
# else:
#     print("we both are of the same age")
# score = int(input("please enter your score from (0 - 100)? "))
# if score >= 90:
#     print("Grade A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 60:
#     print("Grade C")
# elif score >= 40:
#     print("Grade D")
# else:
#     print("Unfortunately you failed this class")
# month = input("Enter the current month ").capitalize()
# if month in ["April", "May", "March"]:
#     print("We are currently in the season of Spring")
# elif month in ["June", "July", "August"]:
#     print("We are currently in the season of Summer")
# elif month in ["September", "October", "November"]:
#     print("We are currently in the season of Autumn")
# elif month in ["December", "January", "February"]:
#     print("We are currently in the season of Winter")
# else:
#     print("The month you entered is invalid")
# fruits = ["banana", "orange", "mango", "lemon"]
# new_fruit = input("Enter  a fruit ").lower()
# if new_fruit in fruits:
#     print("Your fruit already exists")
# else:
#     fruits.append(new_fruit)
#     print(fruits)
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
skills = person["skills"]
if "skills" in person:
    middle_index = len(skills) // 2
    print(skills[middle_index])
if "Python" in skills:
    print("this person knows Python")
if "React" in skills and "Node" in skills and "MongoDB" in skills:
    print("He is a fullstack developer")
elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
    print("He is a Backend developer")
else:
    print("unknown title")
if person["is_married"] is True and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married."
    )
