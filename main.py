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
import numpy as np

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
# BUTTONS_POSITIONS = ((0.5, 0.70),
#                      (0.8, 0.55),
#                      (0.65, 0.35),
#                      (0.35, 0.35),
#                      (0.2, 0.55))

CHOICES_NUMBER = 5
CIRCLE_ORIGIN_X = 0.5
CIRCLE_ORIGIN_Y = 0.5
RADIUS = 0.25


class MainWidget(RelativeLayout):
    result_txt = StringProperty()
    player_name_txt = StringProperty()
    player_score_txt = StringProperty("0")
    ia_name_txt = StringProperty()
    ia_score_txt = StringProperty("0")
    buttons_list = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # Initialize players
        self.player = Player("Player", 0, 0)
        self.ia = Player("I.A.", 0, 0)
        self.player_name_txt = self.player.name
        self.ia_name_txt = self.ia.name
        # Initialize buttons
        self.create_buttons()

    @staticmethod
    def calculate_coordinates_button(button_index):
        angle = (360 / CHOICES_NUMBER * (button_index + 1) + 18) % 360
        x = round(RADIUS * np.cos(np.radians(angle)) + CIRCLE_ORIGIN_X, 2)
        y = round(RADIUS * np.sin(np.radians(angle)) + CIRCLE_ORIGIN_Y, 2)
        x, y = float(x), float(y)
        return x, y

    def create_buttons(self):
        for i in range(0, CHOICES_NUMBER):
            x, y = self.calculate_coordinates_button(i)
            b = Button(
                size_hint=(None, None),
                size=(165, 165),
                pos_hint={"center_x": x, "center_y": y},
                background_normal=NORMAL_IMAGES[i],
                background_down=DOWN_IMAGES[i]
            )
            b.on_press = partial(self.play, i+1)  # Starts from 1-Rock
            self.add_widget(b)
            self.buttons_list.append(b)

    @staticmethod
    def change_button_image(button, mode, index):
        if mode == "normal":
            button.background_normal = NORMAL_IMAGES[index]
        elif mode == "win":
            button.background_normal = WIN_IMAGES[index]
        elif mode == "lose":
            button.background_normal = LOSE_IMAGES[index]
        elif mode == "tie":
            button.background_normal = DOWN_IMAGES[index]

    def update_scores(self):
        self.player_score_txt = str(self.player.score)
        self.ia_score_txt = str(self.ia.score)

    def play(self, selection):
        # Reset images of all buttons
        for i, button in enumerate(self.buttons_list):
            self.change_button_image(button, "normal", i)
        # Plays from players (random in case of computer)
        self.player.play(selection)
        self.ia.play(random.randint(1, CHOICES_NUMBER))
        # print(self.ia.category)  # DEBUG
        result = self.player.compare(self.ia)
        self.update_scores()
        self.result_txt = result[0]
        # print(result)  # DEBUG
        if not result[1] == -1:  # win or lose
            self.change_button_image(self.buttons_list[result[1]], "win", result[1])
            self.change_button_image(self.buttons_list[result[2]], "lose", result[2])
        else:  # tie
            self.change_button_image(self.buttons_list[result[2]], "tie", result[2])


class RpslsApp(App):
    pass


rpsls_app = RpslsApp
rpsls_app().run()
