import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "Role": [
        "AI Engineer",
        "Data Scientist",
        "ML Ops",
        "NLP Specialist",
        "AI Researcher",
    ],
    "Salary": [95000, 88000, 72000, 91000, 105000],
    "Experience_Years": [4, 3, 2, 4, 6],
}
df = pd.DataFrame(data)

print("--- AI Team DataFrame ---")
print(df)
print("\nShape (rows, columns):", df.shape)

print("\n--- Instant Statistics (.describe()) ---")
print(df.describe())

avg_salary = df["Salary"].mean()
print(f"\nAverage Salary: ${avg_salary:.2f}")

df["Bonus"] = df["Salary"] * 0.10
print("\n--- DataFrame with Bonus Column ---")
print(df[["Name", "Salary", "Bonus"]])

high_earners = df[df["Salary"] > 90000]
print("\n--- High Earners (Salary > $90k) ---")
print(high_earners[["Name", "Role", "Salary"]])

df.to_csv("day_25/ai_team.csv", index=False)
print("\nSuccessfully saved data to day_25/ai_team.csv")

print("\n--- Targeted Access ---")
print("Row 1 (Bob's entire record):\n", df.iloc[1])
print("\nExact cell (Charlie's sallary via .loc):", df.loc[2, "Salary"])
print("Exact cell (via .iloc):     ", df.iloc[0, 2])

df["Total_Compensation"] = df["Salary"] + df["Bonus"]
print("\n--- Combined Compensation Column ---")
print(df[["Name", "Salary", "Bonus", "Total_Compensation"]])

df_clean = df.drop(columns=["Bonus"])
print("\n--- After Dropping 'Bonus' Column ---")
print(df_clean.columns.tolist())

print("\n--- Reading back from ai_team.csv ---")
saved_df = pd.read_csv("day_25/ai_team.csv")
print("First two rows (.head()):\n", saved_df.head(2))
