import random

class DiceRoller:
    def roll_dice(self):
        return random.randint(1, 6)

def main():
    dice_roller = DiceRoller()

    print("Welcome to the Dice Rolling Game!")

    while True:
        input("Press Enter to roll the dice...")

        dice_value = dice_roller.roll_dice()
        print(f"You rolled: {dice_value}")

        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
