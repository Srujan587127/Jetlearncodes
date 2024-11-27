game_dict = {
    'Cricket': 'A team sport played with a bat and ball',
    'Football': 'A game played with a round ball on a field',
    'Tennis': 'A racket sport played by two or four players'
}

game_name = input("Enter the name of a game to get its description: ")
if game_name in game_dict:
    print(f"Description of {game_name}: {game_dict[game_name]}")
else:
    print(f"{game_name} is not in the dictionary.")

game_dict['Volleyball'] = 'A sport where teams hit a ball over a net'
print("New game added: Volleyball")

game_dict['Cricket'] = 'A bat-and-ball game played between two teams of 11 players'
print("Updated description for Cricket.")

print("Final Game Dictionary:")
for game, description in game_dict.items():
    print(f"{game} : {description}")
