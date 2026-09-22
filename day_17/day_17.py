countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland", "Estonia", "Russia"]
*nordic_countries, es, ru = countries
print(nordic_countries)
print(es)
print(ru)


def add_three(a, b, c):
    return a + b + c


numbers = 20, 60, 45
print(add_three(*numbers))


def sum_all(*args):
    print("Packed tuple:", args)
    return sum(args)


print(sum_all(8, 78, 7.89, 60))


def user_card(name, country, role):
    return f"👤 {name} ({role}) from {country}"


user_dict = {"name": "Inoy", "country": "India", "role": "AI Engineer"}
print(user_card(**user_dict))

defaults = {"theme": "dark", "volume": 50, "notifications": True}
user_choices = {"volume": 85, "theme": "light"}

final_settings = {**defaults, **user_choices}
print(final_settings)


def configure_model(model_name, **hyperparameters):
    print(f"\n Configuring AI Model : {model_name}")
    for para, value in hyperparameters.items():
        print(f" - {para}: {value}")


configure_model("LinearRegression", learning_rate=0.05, max_iter=1000)
configure_model("DeepNeuralNetwork", layers=5, optimizer="Adam", dropout=0.2, epochs=50)

skills = ["Python", "Machine Learning", "Data Engineering", "Neural Networks"]

for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")

names_02 = ["Inoy", "Sarah", "Alex"]
scores = [95, 88, 92]
roles_02 = ["Lead AI", "Data Analyst", "Backend Engineer"]
for name, score, role in zip(names_02, scores, roles_02):
    print(f"Name {name} | Role {role} | Score: {score}")
