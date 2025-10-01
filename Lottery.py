import random

print("=" * 50)
print("   Harvey mors Corporation")
print("   6/60 Lottery Game")
print("=" * 50)
print("\nWelcome to the 6/60 Lottery!")
print("Pick 6 numbers from 1 to 60")
print("Play slip cost: ₱20\n")

winning_numbers = sorted(random.sample(range(1, 61), 6))
player_numbers = []

for i in range(6):
    while True:
        num = int(input(f"Enter number {i+1}: "))
        if 1 <= num <= 60:
            if num not in player_numbers:
                player_numbers.append(num)
                break
            else:
                print("Number already chosen. Pick a different number.")
        else:
            print("Invalid! Enter a number between 1 and 60.")

player_numbers.sort()

matched_numbers = [num for num in player_numbers if num in winning_numbers]
matches = len(matched_numbers)

print("\n" + "=" * 50)
print("LOTTERY RESULTS")
print("=" * 50)
print(f"Winning Numbers: {winning_numbers}")
print(f"Your Numbers: {player_numbers}")
print(f"\nMatched Numbers: {matched_numbers}")
print(f"Total Matches: {matches}\n")

if matches == 6:
    prize = 1000000
    print("CONGRATULATIONS! YOU WON THE JACKPOT!")
else:
    prize = matches * 1000

print(f"Total Prize: ₱{prize:,}")
print("=" * 50)