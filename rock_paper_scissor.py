import random

choices = ["rock", "paper", "scissors"]
print("🪨📄✂️ ROCK, PAPER, SCISSORS GAME! 🪨📄✂️")

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print(f"🤖 Computer chose: {computer}")

if user == computer:
    print("🤝 It's a tie!")
elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print("🎉 You win! ✨")
else:
    print("💀 Computer wins! Better luck next time.")