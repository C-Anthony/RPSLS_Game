""" RPSLS as per Rock, Paper, Scissors, Lizard, Spock Game
    Based on The Big Bang Theory serie game, expansion of the basic Rock Paper Scissors game
"""
# Config
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '1200')
# Config.set('kivy', 'window_icon', "resources/icon2.png")
# Imports
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from player import Player
import random
from functools import partial

# Constants
NORMAL_IMAGES = ("resources/images/Rock.png",
                 "resources/images/Paper.png",
                 "resources/images/Scissors.png",
                 "resources/images/Lizard.png",
                 "resources/images/Spock.png")
DOWN_IMAGES = ("resources/images/Rock_down.png",
               "resources/images/Paper_down.png",
               "resources/images/Scissors_down.png",
               "resources/images/Lizard_down.png",
               "resources/images/Spock_down.png")
WIN_IMAGES = ("resources/images/Rock_green.png",
              "resources/images/Paper_green.png",
              "resources/images/Scissors_green.png",
              "resources/images/Lizard_green.png",
              "resources/images/Spock_green.png")
LOSE_IMAGES = ("resources/images/Rock_red.png",
               "resources/images/Paper_red.png",
               "resources/images/Scissors_red.png",
               "resources/images/Lizard_red.png",
               "resources/images/Spock_red.png")
BUTTONS_POSITIONS = ((0.5, 0.70),
                     (0.8, 0.55),
                     (0.65, 0.35),
                     (0.35, 0.35),
                     (0.2, 0.55))


class MainWidget(RelativeLayout):
    result_txt = StringProperty()
    player_name_txt = StringProperty()
    player_score_txt = StringProperty("0")
    ia_name_txt = StringProperty()
    ia_score_txt = StringProperty("0")
    buttons_list = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.player = Player("Player", 0, 0)
        self.ia = Player("I.A.", 0, 0)
        self.player_name_txt = self.player.name
        self.ia_name_txt = self.ia.name
        self.create_buttons()

    def create_buttons(self):
        for i in range(0, 5):
            b = Button(
                size_hint=(0.25, 0.15),
                pos_hint={"center_x": BUTTONS_POSITIONS[i][0], "center_y": BUTTONS_POSITIONS[i][1]},
                background_normal=NORMAL_IMAGES[i],
                background_down=DOWN_IMAGES[i]
            )
            b.on_press = partial(self.play, i+1)
            self.add_widget(b)
            self.buttons_list.append(b)

    def play(self, selection):
        for i, button in enumerate(self.buttons_list):
            button.background_normal = NORMAL_IMAGES[i]
        self.player.play(selection)
        self.ia.play(random.randint(1, 5))
        # print(self.ia.category)  # DEBUG
        result = self.player.compare(self.ia)
        self.update_scores()
        self.result_txt = result[0]
        # print(result)  # DEBUG
        if not result[1:] == (0, 0):
            self.buttons_list[result[1]].background_normal = WIN_IMAGES[result[1]]
            self.buttons_list[result[2]].background_normal = LOSE_IMAGES[result[2]]

    def update_scores(self):
        self.player_score_txt = str(self.player.score)
        self.ia_score_txt = str(self.ia.score)


class RpslsApp(App):
    pass


rpsls_app = RpslsApp
rpsls_app().run()
