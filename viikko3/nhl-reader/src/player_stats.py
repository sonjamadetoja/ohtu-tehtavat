from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player_dict in self.reader.get_players():
            nat = player_dict['nationality']

            if nat == nationality:
                name = player_dict['name']
                team = player_dict['team']
                goals = player_dict['goals']
                assists = player_dict['assists']
                points = goals+assists
                player = Player(
                    name, nat, team, goals, assists, points
                )
                players.append(player)

        players.sort(key=lambda player: player.points, reverse=True)

        return players