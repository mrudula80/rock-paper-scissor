import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")
    else:
        print("😢 Computer wins!")

    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break_