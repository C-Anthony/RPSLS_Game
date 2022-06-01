# Imports
from itertools import chain


class Player:
    score = 0
    category = []
    categories = [
        ["Not defined"],                                    # 0
        ["Rock", ["crushes", 3], ["crushes", 4]],           # 1
        ["Paper", ["covers", 1], ["disproves", 5]],         # 2
        ["Scissors", ["cuts", 2], ["decapitates", 4]],      # 3
        ["Lizard", ["eats", 2], ["poisons", 5]],            # 4
        ["Spock", ["smashes", 1], ["vaporizes", 3]]         # 5
    ]

    def __init__(self, name, category, score):
        self.name = name
        self.category = self.categories[category]
        self.score = score

    def play(self, category):
        self.category = self.categories[category]

    def find_players_indexes(self, opponent):
        """ Find players indexes in the categories, permitting its use through the program.
            returns index of the player, index of the computer """
        index_player = 0
        index_opponent = 0
        for index, category in enumerate(self.categories):
            if self.category == category:
                index_player = index - 1
            if opponent.category == category:
                index_opponent = index - 1
        return index_player, index_opponent

    def find_index_for_txt(self, winner_category, loser_category):
        """ Find index in the player or the IA category in order to express correctly how the winner wins
            for example: 'crushes' if it is rock vs scissors.
            returns the index of the category containing the correct word
        """
        index_found = 0
        for index, category_list in enumerate(winner_category):
            if category_list[1] == self.categories.index(loser_category):
                index_found = index
        return index_found

    def compare(self, opponent):
        """ Compare self.category to opponent.category, checking if one is in the category of the other
            meaning that the one containing the other is the winner. If categories are the same,
            this is a tie.
            returns a string with "winner beats loser" with appropriate words, the index of the winner,
            and the index of the loser. In case of a tie, returns the string with 'equals', -1,
            and the selection of both players.
        """
        if opponent.category == self.category:  # tie - no change in score
            index_player, index_opponent = self.find_players_indexes(opponent)
            # print(f"{self.category[0]} equals {opponent.category[0]}")  # DEBUG
            result_str = self.category[0] + "  equals  " + opponent.category[0]
            return result_str, -1, index_player

        elif self.categories.index(opponent.category) in chain.from_iterable(self.category):  # player wins
            self.score += 1
            index_found = self.find_index_for_txt(self.category, opponent.category)
            index_player, index_opponent = self.find_players_indexes(opponent)
            # print(f"{self.category[0]} {self.category[index_found][0]} {opponent.category[0]}")  # DEBUG
            result_str = self.category[0] + "  " + self.category[index_found][0] + "  " + opponent.category[0]
            return result_str, index_player, index_opponent

        # I.A. wins
        opponent.score += 1
        index_found = self.find_index_for_txt(opponent.category, self.category)
        index_player, index_opponent = self.find_players_indexes(opponent)
        # print(f"{opponent.category[0]} {opponent.category[index_found][0]} {self.category[0]}")  # DEBUG
        result_str = opponent.category[0] + "  " + opponent.category[index_found][0] + "  " + self.category[0]
        return result_str, index_opponent, index_player
