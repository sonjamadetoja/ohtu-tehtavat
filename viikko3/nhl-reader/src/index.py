import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        nat = player_dict['nationality']

        if nat == "FIN":
            name = player_dict['name']
            team = player_dict['team']
            goals = player_dict['goals']
            assists = player_dict['assists']
            combined = goals+assists
            player = Player(
                name, nat, team, goals, assists, combined
            )
            players.append(player)

    print("Oliot:")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
