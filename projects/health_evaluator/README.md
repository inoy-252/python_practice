# 🩺 Health Evaluator & Biometric Scorecard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Domain](https://img.shields.io/badge/Domain-Digital%20Health%20%26%20Biometrics-red.svg)](#)

A command-line biometric calculator and personal health diagnostic scorecard written in Python. This tool computes essential physical fitness metrics, cardiovascular training zones, hydration guidelines, and classification flags from user inputs.

---

## 🌟 Key Features & Computed Metrics

| Metric | Formula / Logic | Description |
| :--- | :--- | :--- |
| **Body Mass Index (BMI)** | $\text{weight (kg)} / \text{height (m)}^2$ | Evaluates body mass relative to height; flags healthy weight range ($20 \le \text{BMI} \le 24$). |
| **Max Heart Rate (MHR)** | $220 - \text{age}$ | Standard physiological estimate of maximum safe cardiac exertion. |
| **Target Cardio Zone** | $0.70 \times \text{MHR}$ | Ideal heart rate zone for aerobic cardiovascular endurance. |
| **Daily Water Intake** | $\text{weight (kg)} \times 0.033\text{ L}$ | Recommended daily fluid intake based on body weight. |
| **Biometric Flags** | Conditional logic | Evaluates age categories, senior citizen cardiac status, and detects professional medical titles (`Dr.`). |

---

## 💻 Quickstart & Usage

No third-party packages required—runs on standard Python!

```bash
# Clone repository
git clone https://github.com/inoy-252/bmi-health-evaluator.git
cd bmi-health-evaluator

# Run the health evaluator
python app.py
```

### 💡 Example Interactive Session:

```text
What is your name? Dr. Inoy
What is your age? 24
Enter your weight in kgs? 68.5
Please mention your height in meters? 1.78

========================================
HEALTH SCORECARD OF DR. INOY 
Your name is Dr. Inoy
You are 24 years old
You are 1.78 mtrs tall
You weigh 68.5 kgs
your bmi is 21.6	You should drink 2.26 ltrs of water
You are an adult True
you are a medical proffessional True
Max heart rate: 196 bpm	Target Cardio Zone: 137 bpm
========================================
```

---

## 📂 File Structure

```text
bmi-health-evaluator/
├── app.py         # Main biometric scorecard engine
├── .gitignore     # Standard Python ignore rules
└── README.md      # Project documentation
```

---

## 🔮 Roadmap / Future Improvements

- [ ] Add BMI category breakdown (Underweight, Normal, Overweight, Obese) based on WHO guidelines.
- [ ] Add Basal Metabolic Rate (BMR) calculation via the Mifflin-St Jeor equation.
- [ ] Implement a rich terminal UI with colored status badges (using `rich` or `curses`).

---

## 👤 Author

**Yasir Lone ([@inoy-252](https://github.com/inoy-252))**
