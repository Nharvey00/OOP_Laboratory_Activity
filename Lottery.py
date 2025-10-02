import random

class LotteryGame:
    def __init__(self):
        self.winning_numbers = set(random.sample(range(1, 61), 6))
        self.player_numbers = set()
    
    def set_player_numbers(self, numbers):
        if len(numbers) == 6 and all(1 <= n <= 60 for n in numbers) and len(set(numbers)) == 6:
            self.player_numbers = set(numbers)
            return True
        return False
    
    def calculate_prize(self):
        matches = len(self.winning_numbers & self.player_numbers)
        return 1000000 if matches == 6 else matches * 1000
    
    def display_results(self):
        matches = len(self.winning_numbers & self.player_numbers)
        prize = self.calculate_prize()
        
        print("\n" + "=" * 60)
        print("LOTTERY 6/60 RESULTS")
        print("=" * 60)
        print(f"Winning Numbers: {sorted(self.winning_numbers)}")
        print(f"Your Numbers:    {sorted(self.player_numbers)}")
        print(f"Matches: {matches}/6")
        print(f"Prize: ₱{prize:,}" + (" - JACKPOT!" if matches == 6 else ""))
        print("=" * 60 + "\n")


# Usage
print("=" * 60)
print("LOTTERY GAME 6/60")
print("=" * 60)
print("Enter 6 numbers (1-60):\n")

lottery = LotteryGame()
player_numbers = []

while len(player_numbers) < 6:
    try:
        num = int(input(f"Number {len(player_numbers) + 1}: "))
        if num < 1 or num > 60:
            print("Invalid! Must be 1-60.")
        elif num in player_numbers:
            print("Duplicate!")
        else:
            player_numbers.append(num)
    except ValueError:
        print("Invalid input.")

if lottery.set_player_numbers(player_numbers):
    lottery.display_results()
