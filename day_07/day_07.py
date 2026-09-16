it_companies = {"google", "microsoft", "apple"}
print("starting companies:", it_companies)
print("count", len(it_companies))
it_companies.add("nvidia")
print("after adding nvidia:", it_companies)
it_companies.add("google")
print("after adding google again", it_companies)
ages_list = (34, 23, 23, 45, 21, 34, 22, 21, 16, 18, 19, 18)
unique_ages = set(ages_list)
print("original list:", ages_list)
print("unique set:", unique_ages)
print("original count:", len(ages_list))
print("unique count:", len(unique_ages))
python_devs = {"python", "git", "sql", "docker"}
ai_devs = {"python", "math", "pytorch", "git"}
print("skills of a python dev:", python_devs)
print("skills of an ai dev:", ai_devs)
common_skills = python_devs.intersection(ai_devs)
print("common skills:", common_skills)
all_skills = python_devs.union(ai_devs)
print("all skills:", all_skills)
only_python = python_devs.difference(ai_devs)
print("skills only python devs have:", only_python)
sentence = (
    "I am a teacher who teaches the subject english and I love this profession of mine"
)
words_list = sentence.split()
unique_words = set(words_list)
print("the number of unique words in sentence", sentence, "are", len(unique_words))
