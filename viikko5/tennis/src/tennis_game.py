class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0
        self.tie_dict = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }
        self.update_score_dict = {
            0:"Love",
            1:"Fifteen",
            2:"Thirty",
            3:"Forty"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.score_player1 = self.score_player1 + 1
        else:
            self.score_player2 = self.score_player2 + 1

    def get_score(self):
        if self.score_player1 == self.score_player2:
            return self.tie()
        elif self.score_player1 >= 4 or self.score_player2 >= 4:
            return self.more_than_four_points()
        else:
            return self.not_tie_and_less_than_four_points()

    def tie(self):
        if self.score_player1 in self.tie_dict:
            return self.tie_dict[self.score_player1]
        else:
            return "Deuce"

    def more_than_four_points(self):
        minus_result = self.score_player1 - self.score_player2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def not_tie_and_less_than_four_points(self):
        return self.update_score(self.score_player1) + "-" + self.update_score(self.score_player2)

    def update_score(self, new_score):
        return self.update_score_dict[new_score]
