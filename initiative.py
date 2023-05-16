import math

from character import Character


class Initiative:
    def __init__(self, characters, window_size):
        self.start = True
        self.actor_index = 0
        self.turn = 1
        self.window_size = window_size
        self.half_point = math.floor(window_size / 2)
        parsed_characters = [Character(**character_data) for character_data in characters]
        self.characters = sorted(parsed_characters, key=lambda character: character.roll, reverse=True)

    def next(self):
        self.actor_index = (self.actor_index + 1) % len(self.characters)
        if self.actor_index == 0:
            self.turn = self.turn + 1
        if self.turn > 1 or self.actor_index >= self.half_point:
            self.start = False

    def actor(self, index_modifier=0):
        if self.start and index_modifier < -self.actor_index:
            return None
        return self.characters[(self.actor_index + index_modifier) % len(self.characters)]

    def previous(self):
        if self.turn == 1 and self.actor_index == 0:
            self.start = True
            return
        self.actor_index = (self.actor_index - 1) % len(self.characters)
        if self.actor_index == (len(self.characters) - 1):
            self.turn = self.turn - 1

    def reset(self):
        self.start = True
        self.actor_index = 0
        self.turn = 1
