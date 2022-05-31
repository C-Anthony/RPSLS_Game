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

    def find_indexes(self, opponent):
        index_player = 0
        index_opponent = 0
        for index, category in enumerate(self.categories):
            if self.category == category:
                index_player = index - 1
            if opponent.category == category:
                index_opponent = index - 1
        return index_player, index_opponent

    def compare(self, opponent):
        index_found = 0

        if opponent.category == self.category:  # tie - no change in score
            # print(f"{self.category[0]} equals {opponent.category[0]}")  # DEBUG
            result_str = self.category[0] + "  equals  " + opponent.category[0]
            return result_str, 0, 0

        elif self.categories.index(opponent.category) in chain.from_iterable(self.category):  # player wins
            self.score += 1

            for index, category_list in enumerate(self.category):
                if category_list[1] == self.categories.index(opponent.category):
                    index_found = index
            index_player, index_opponent = self.find_indexes(opponent)
            # print(f"{self.category[0]} {self.category[index_found][0]} {opponent.category[0]}")  # DEBUG
            result_str = self.category[0] + "  " + self.category[index_found][0] + "  " + opponent.category[0]
            return result_str, index_player, index_opponent

        # I.A. wins
        opponent.score += 1

        for index, category_list in enumerate(opponent.category):
            if category_list[1] == self.categories.index(self.category):
                index_found = index
        index_player, index_opponent = self.find_indexes(opponent)
        # print(f"{opponent.category[0]} {opponent.category[index_found][0]} {self.category[0]}")  # DEBUG
        result_str = opponent.category[0] + "  " + opponent.category[index_found][0] + "  " + self.category[0]
        return result_str, index_opponent, index_player
