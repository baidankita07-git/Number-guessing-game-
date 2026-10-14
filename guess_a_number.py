import random

secret_num = random.randint(1, 20)
print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮\n🛸 I am thinking of a number between 1 and 20.")

while True:
    guess = int(input("\n🔮 Take a guess: "))
    if guess < secret_num:
        print("📉 Too low! Try a higher number.")
    elif guess > secret_num:
        print("📈 Too high! Try a lower number.")
    else:
        print(f"🎉 CONGRATULATIONS! You found the secret number: {secret_num}! ✨")
        break
