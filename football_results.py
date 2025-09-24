first_game: str = str(input())
second_game: str = str(input())
third_game: str = str(input())

games_won: int = 0
games_lost: int = 0
game_draw: int = 0

tournament: list = [first_game, second_game, third_game]

for game in tournament:
    goals_scored, goals_conceived = game.split(':')
    if goals_scored > goals_conceived:
        games_won += 1
    elif goals_scored < goals_conceived:
        games_lost += 1
    else:
        game_draw += 1

print(f'Team won {games_won} games.')
print(f'Team lost {games_lost} games.')
print(f'Drawn games: {game_draw}')