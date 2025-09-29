total_people_count = int(input())
counter:int = 1

fitness = {
    "Back": 0,
    "Chest": 0,
    "Legs": 0,
    "Abs": 0,
    "Protein shake": 0,
    "Protein bar": 0
}

for _ in range(total_people_count):
    action_type = input().strip()
    fitness[action_type] += 1   # вече винаги съществува ключът
people_training = fitness["Back"] + fitness["Chest"] + fitness["Legs"] + fitness["Abs"]
protein_buyers = fitness["Protein shake"] + fitness["Protein bar"]

print(f'{fitness.get("Back")} - back')
print(f'{fitness.get("Chest")} - chest')
print(f'{fitness.get("Legs")} - legs')
print(f'{fitness.get("Abs")} - abs')
print(f'{fitness.get("Protein shake")} - protein shake')
print(f'{fitness.get("Protein bar")} - protein bar')
print(f'{(people_training/total_people_count) * 100:.2f}% - work out')
print(f'{(protein_buyers/total_people_count) * 100:.2f}% - protein')

