player_name: str = str(input())
points:int = 301
successful_shots:int = 0
unsuccessful_shots:int = 0


while True:
    field_type: str = str(input())

    if field_type == 'Retire':
        print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
        break
    score: int = int(input())

    if field_type == 'Single':
        shot_score = score
    elif field_type == 'Double':
        shot_score = score * 2
    elif field_type == 'Triple':
        shot_score = score * 3
    else:
        continue

    if shot_score > points:
        unsuccessful_shots += 1
        continue
    else:
        points -= shot_score
        successful_shots += 1
    if points == 0:
        print(f'{player_name} won the leg with {successful_shots} shots.')
        break
