tennis_raq_price: float = float(input())
count_tennis_raq: int = int(input())
count_sneakers: int = int(input())


sneaker_price: float = (1/6)*tennis_raq_price

raquets_and_sneakers_price = ((count_tennis_raq * tennis_raq_price) + (count_sneakers * sneaker_price))
other_equipment = raquets_and_sneakers_price * 0.2

total_price = raquets_and_sneakers_price + other_equipment

player_bill:float = (total_price / 8).__floor__()

sponsor_bill:float = (total_price * (7/8)).__ceil__()

print(f'Price to be paid by Djokovic {player_bill}')
print(f'Price to be paid by sponsors {sponsor_bill}')