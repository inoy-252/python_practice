name = input("What is your name? ")
age = int(input("What is your age? "))
weight = float(input("Enter your weight in kgs? "))
height = float(input("Please mention your height in meters? "))
bmi = (weight) / (height) ** 2
max_heart_rate = 220 - age
target_cardio_hr = 0.7 * max_heart_rate
daily_water_intake = weight * 0.033
is_normal_weight = bmi >= 20 and bmi <= 24
is_adult = age >= 18
is_old_citiezen = age > 40 or max_heart_rate < 165
name_clean = name.lower()
has_medical_title = "dr" in name_clean or "doctor" in name
print("=" * 40)
print(f"HEALTH SCORECARD OF {name.upper()} ")
print(
    f"Your name is {name}\nYou are {age} years old\nYou are {height} mtrs tall\nYou weigh {weight} kgs"
)
print(f"your bmi is {bmi:.1f}\tYou should drink {daily_water_intake:.2f} ltrs of water")
print(f"You are an adult {is_adult}")
print(f"you are a medical proffessional {has_medical_title}")
print(
    f"Max heart rate: {max_heart_rate} bpm\tTarget Cardio Zone: {target_cardio_hr:.0f} bpm"
)
print("=" * 40)
