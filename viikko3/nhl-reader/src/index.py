import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        nat = player_dict['nationality']

        if nat == "FIN":
            name = player_dict['name']
            team = player_dict['team']
            goals = player_dict['goals']
            assists = player_dict['assists']
            points = goals+assists
            player = Player(
                name, nat, team, goals, assists, points
            )
            players.append(player)

    print("Oliot:")

    players.sort(key=lambda player: player.points, reverse=True)

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
