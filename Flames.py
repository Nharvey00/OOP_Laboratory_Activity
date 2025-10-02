class FlamesGame:
    FLAMES = {'F': 'Friendship', 'L': 'Love', 'A': 'Affection', 
              'M': 'Marriage', 'E': 'Enemy', 'S': 'Sibling'}
    
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
    
    def _remove_common_letters(self):
        list1 = list(self.name1.lower().replace(" ", ""))
        list2 = list(self.name2.lower().replace(" ", ""))
        
        for letter in list(list1):
            if letter in list2:
                list1.remove(letter)
                list2.remove(letter)
        
        return len(list1) + len(list2)
    
    def _eliminate(self, count):
        flames = ['F', 'L', 'A', 'M', 'E', 'S']
        index = 0
        
        while len(flames) > 1:
            index = (index + count - 1) % len(flames)
            flames.pop(index)
        
        return flames[0]
    
    def calculate(self):
        count = self._remove_common_letters()
        
        if count == 0:
            return "Not compatible! Single forever </3"
        
        return self.FLAMES[self._eliminate(count)]


# Usage
print("=" * 40)
print("   FLAMES - Mating Game")
print("=" * 40)
print()

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

game = FlamesGame(name1, name2)
print()
print(f"Result: {game.calculate()}")
print()
