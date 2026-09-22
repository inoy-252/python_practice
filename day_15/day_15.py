# total = "50" + 10
# print(total)
# languages = ["python", "C", "javascript"]
# print(languages[10])
# user = {"name": "Inoy", "country": "India"}
# print(user["email"])
# try:
#     age = int(input("what is your age? "))
#     print("you are", age, "years old")
# except ValueError:
#     print("please enter numbers only (e.g. 25), not words!")


# def safe_divide(a, b):
#     try:
#         return a / b
#     except Exception as e:
#         return f"Math failed! Python says: {e}"


# print(safe_divide(8, 4))
# print(safe_divide(4, 0))
# print(safe_divide("eight", 8))

# try:
#     num = int("hello")
# except Exception as e:
#     print(f"Caught an error: {e}")


try:
    number = int(input("Enter an even number: "))
    if number % 2 != 0:
        raise ValueError("That is an odd number! Even numbers only please.")
    result = 100 / number
except ZeroDivisionError:
    print("Error: You cannot divide by zero")
except Exception as e:
    print("General error!", e)
else:
    print(f"Success 100 / {number} = {result:.2f}")
finally:
    print("Transaction session ended. Thank you!")
