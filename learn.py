import random

money = int(input("How much money do you want to bet? "))

while True:
    side = input("Do you want to bet on heads or tails? ").lower()
    
    if side not in ['heads', 'tails']:
        print("Invalid choice. Try again.")
        continue

    input("Press Enter to flip the coin...")

    coin = random.choice(['heads', 'tails'])
    print(f"The coin landed on {coin}.")

    if coin == side:
        money *= 2
        print(f"You won! You now have {money}.")
    else:
        money /= 2
        print(f"You lost. You now have {money}.")

    interest = input("Do you want to play again? (yes/no) ").lower()
    if interest != "yes":
        print("Thanks for playing! Goodbye!")
        break