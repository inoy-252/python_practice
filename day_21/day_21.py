class AIModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.chat_history = []
        self.total_queries = 0

    def generate_response(self, prompt):
        return f"[{self.name} v{self.version}] Proccessing '{prompt}' ... Done! "

    def chat(self, user_message):
        self.chat_history.append(user_message)
        self.total_queries += 1
        reply = self.generate_response(user_message)
        return reply


model_1 = AIModel("Llama", 3.1)
model_2 = AIModel("DeepSeek", 2.5)

print(f"Model 1: {model_1.name} v{model_1.version}")
print(f"Model 2: {model_2.name} v{model_2.version}")

print(model_1.chat("What is Python"))
print(model_1.chat("Explain Gravity"))

print(model_2.chat("Who is Gojo Satarou"))

print("Model 1 memory ")
print("History:", model_1.chat_history)
print("Total Queries", model_1.total_queries)

print("Model 2 memory")
print("History:", model_2.chat_history)
print("Total Queries:", model_2.total_queries)


class visionmodel(AIModel):
    def analyze_image(self, image_url):
        self.total_queries += 1
        self.chat_history.append(f"Image Analysis: {image_url}")

        return f"{self.name} Analyzing image at '{image_url}' ... Detected: The image contains......"


vision_bot = visionmodel("GPT-Vision", 4.0)
print(vision_bot.chat("Yare Yare"))
print(vision_bot.analyze_image("https://example.com/dog.jpg"))

print("Vision bot chat history", vision_bot.chat_history)
print("Total Queries:", vision_bot.total_queries)


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 != 0:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def mode(self):
        counts = {x: self.data.count(x) for x in set(self.data)}
        winning_number = max(counts, key=counts.get)
        return {"Mode": winning_number, "count": counts[winning_number]}


ages = [31, 26, 34, 56, 27, 22, 25, 34, 24, 20, 26, 34]
data = Statistics(ages)
print("\n--- Statistics Summary ---")
print("Count: ", data.count())
print("Sum:   ", data.sum())
print("Min:   ", data.min())
print("Max:   ", data.max())
print("Range: ", data.range())
print(f"Mean:   {data.mean():.2f}")
print("Median:   ", data.median())
print("Mode:      ", data.mode())
