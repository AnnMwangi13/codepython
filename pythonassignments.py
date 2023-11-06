# #Even or odd number
# number = int(input("Enter a number: "))
#
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#



# # Asking the user for their age and providing a message
# age = int(input("Enter your age: "))
#
# if age < 13:
#     print("You are a child")
# elif age < 20:
#     print("You are a teenager")
# else:
#     print("You are an adult")



# Converting numerical grade to letter grade
# grade = int(input("Enter your numerical grade (0-100): "))
#
# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")



# Finding the largest number among three
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
#
# if num1 >= num2 and num1 >= num3:
#     print("The largest number is:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The largest number is:", num2)
# else:
#     print("The largest number is:", num3)



## Simulating user authentication
# username = input("Enter your username: ")
# password = input("Enter your password: ")
#
# if username == "your_username" and password == "your_password":
#     print("Welcome, " + username + "!")
# else:
#     print("Access denied")


##Leap year checker
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# # Checking if a number is within the range [1, 10]
# number = int(input("Enter a number: "))
#
# if 1 <= number <= 10:
#     print("In range")
# else:
#     print("Out of range")


# # Checking if a number is positive, negative, or zero
# number = float(input("Enter a number: "))
#
# if number > 0:
#     print("Positive number")
# elif number < 0:
#     print("Negative number")
# else:
#     print("Zero")



# # Temperature conversion program
# choice = input("Choose conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter 1 or 2: ")
#
# if choice == '1':
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C is equal to {fahrenheit}°F")
# elif choice == '2':
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = (fahrenheit - 32) * 5/9
#     print(f"{fahrenheit}°F is equal to {celsius}°C")
# else:
#     print("Invalid choice")



# # Discount calculator
# price = float(input("Enter the price of the item: "))
# threshold = 100  # Set the threshold for discount
#
# if price > threshold:
#     discount_percentage = 10  # 10% discount if the price is above the threshold
#     discount = (discount_percentage / 100) * price
#     discounted_price = price - discount
#     print(f"Discounted price: ${discounted_price:.2f}")
# else:
#     print(f"No discount applied. Price: ${price:.2f}")



# # Vowel or consonant checker
# char = input("Enter a character: ").lower()  # Convert to lowercase for case insensitivity
#
# if char.isalpha() and len(char) == 1:
#     if char in "aeiou":
#         print(f"{char} is a vowel.")
#     else:
#         print(f"{char} is a consonant.")
# else:
#     print("Invalid input. Please enter a single alphabet character.")



# import math
#
# # Quadratic equation solver
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
#
# discriminant = b**2 - 4*a*c
#
# if discriminant > 0:
#     root1 = (-b + math.sqrt(discriminant)) / (2*a)
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print(f"Two real and distinct roots: {root1}, {root2}")
# elif discriminant == 0:
#     root = -b / (2*a)
#     print(f"One real root (repeated): {root}")
# else:
#     real_part = -b / (2*a)
#     imag_part = math.sqrt(-discriminant) / (2*a)
#     print(f"Two complex roots: {real_part} + {imag_part}i, {real_part} - {imag_part}i")
#
#



# # Palindrome checker
# text = input("Enter a word or phrase: ").lower()  # Convert to lowercase for case insensitivity
#
# # Remove spaces and check if the text is the same forwards and backwards
# text = ''.join(text.split())  # Remove spaces
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")



import random

# # Rock, Paper, Scissors game
# options = ["rock", "paper", "scissors"]
# computer_choice = random.choice(options)
# user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#
# print(f"Computer chose: {computer_choice}")
# print(f"You chose: {user_choice}")
#
# if user_choice in options:
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win!")
#     else:
#         print("Computer wins!")
# else:
#     print("Invalid choice. Please choose from rock, paper, or scissors.")
#



# # BMI calculator and health classification
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
#
# bmi = weight / (height ** 2)
#
# print(f"Your BMI is {bmi:.2f}")
#
# if bmi < 18.5:
#     print("Underweight")
# elif 18.5 <= bmi < 24.9:
#     print("Normal weight")
# elif 25 <= bmi < 29.9:
#     print("Overweight")
# else:
#     print("Obese")


import random

# # Guess the number game
# target = random.randint(1, 100)
#
# while True:
#     guess = int(input("Guess a number between 1 and 100: "))
#     if guess < target:
#         print("Too low!")
#     elif guess > target:
#         print("Too high!")
#     else:
#         print("Correct! The number was", target)
#         break



# # Eligibility for voting and driving
# age = int(input("Enter your age: "))
# citizenship = input("Are you a citizen (yes or no): ").lower()
# violations = int(input("Number of previous violations: "))
#
# if age >= 18 and citizenship == "yes" and violations <= 5:
#     print("You are eligible to vote and drive.")
# else:
#     print("You are not eligible to vote and drive.")
