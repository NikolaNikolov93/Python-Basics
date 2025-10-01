projection_type:str = str(input())
rows:int = int(input())
columns:int = int(input())
income:float = 0

if projection_type == "Premiere":
    income = columns * rows * 12
elif projection_type == "Normal":
    income = rows * columns * 7.5
elif projection_type == "Discount":
    income = rows * columns * 5

print(f'{income:.2f} leva')