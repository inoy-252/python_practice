import csv
import json

with open("day_19/test.txt", "w") as f:
    f.write("Hello from day 19!")
with open("day_19/test.txt", "r") as f:
    content = f.read()
print("The contents of the file are as: ", content)

with open("day_19/test.txt", "a") as f:
    f.write("\nAgainst All Odds, I  Bet On Myself  ")
with open("day_19/test.txt", "r") as f:
    content = f.read()
    print(content)


def count_file_stats(filepath):
    num_line = 0
    num_words = 0

    with open(filepath, "r") as f:
        for line in f:
            num_line += 1
            words = line.split()
            num_words += len(words)
    print("--- File Statistics ---")
    print("Total lines: ", num_line)
    print("Total words: ", num_words)


count_file_stats("day_19/test.txt")


model_config = {
    "model_name": "Llama-3-FineTuned",
    "learning_rate": 0.0005,
    "epochs": 20,
    "batch_size": 32,
    "layers": ["Input", "Dense_128", "Dense_64", "Output"],
    "is_active": True,
}

with open("day_19/config.json", "w") as f:
    json.dump(model_config, f, indent=4)
print("config successfully saved to config.json")

with open("day_19/config.json", "r") as f:
    loaded_config = json.load(f)

print("--- Loaded JSON Config ---")
print("Model Name:", loaded_config["model_name"])
print("Learning Rate:", loaded_config["learning_rate"])
print("Is Active:", loaded_config["is_active"])


dataset_rows = [
    ["user_id", "prompt_tokens", "completion_tokens", "latency_ms"],
    ["usr_101", 120, 45, 310],
    ["usr_102", 540, 180, 850],
    ["usr_103", 85, 30, 220],
]

with open("day_19/ai_usage.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dataset_rows)

print("\n Dataset successfully created at ai_usage.csv")

with open("day_19/ai_usage.csv", "r") as f:
    reader = csv.DictReader(f)
    print("--- AI Usage Records ---")
    for row in reader:
        print(
            f"User {row['user_id']}: {row['latency_ms']}ms latency | Total tokens: {int(row['prompt_tokens']) + int(row['completion_tokens'])}"
        )
