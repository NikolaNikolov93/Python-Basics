total_games = 0
wins = 0
losses = 0

while True:
    tournament_name = str(input())
    if tournament_name == "End of tournaments":
        break
    tournament_games: int = int(input())

    for game_number in range(1, tournament_games + 1):
        desi_team_score = int(input())
        other_team_score = int(input())
        total_games += 1

        if desi_team_score > other_team_score:
            wins += 1
            difference = desi_team_score - other_team_score
            print(f"Game {game_number} of tournament {tournament_name}: win with {difference} points.")
        else:
            losses += 1
            difference = other_team_score - desi_team_score
            print(f"Game {game_number} of tournament {tournament_name}: lost with {difference} points.")

win_percentage = (wins / total_games) * 100
loss_percentage = (losses / total_games) * 100
print(f"{win_percentage:.2f}% matches win")
print(f"{loss_percentage:.2f}% matches lost")
