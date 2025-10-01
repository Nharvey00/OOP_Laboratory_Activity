def flames_game(name1, name2):
    list1 = list(name1.lower().replace(" ", ""))
    list2 = list(name2.lower().replace(" ", ""))
    
    for letter in list(list1):
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)
    
    count = len(list1) + len(list2)
    
    if count == 0:
        return "Not compatible! Single forever </3"
    
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    index = 0
    
    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)
    
    flames_dict = {'F': 'Friendship', 'L': 'Love', 'A': 'Affection', 'M': 'Marriage', 'E': 'Enemy', 'S': 'Sibling'}
    
    return flames_dict[flames[0]]

print("=" * 40)
print("   FLAMES - Mating Game")
print("=" * 40)
print()

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

print()
print(f"Result: {flames_game(name1, name2)}")
print()