import random

print("🎯 Welcome to Guess The Number Game!")
print("I am thinking of a number between 1 and 100.")

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    # kiểm tra nhập đúng số
    if not guess.isdigit():
        print("❌ Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Too small ⬆️ Try again!")
    elif guess > secret:
        print("Too big ⬇️ Try again!")
    else:
        print(f"🎉 Correct! The number was {secret}")
        print(f"You guessed in {attempts} attempts.")
        break
