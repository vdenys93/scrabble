import pygame
from .tile import Tile


"""
Author:Team 4
Program:player.py
Player class
"""
class Player:
    PLAYER_NUM = (1, 2, 3, 4)

    """Player class"""
    def __init__(self, nick_name, player_num, turn_count=0, turn_since_last_placement=0, score=0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(nick_name)):
            raise ValueError
        if player_num not in self.PLAYER_NUM:
            raise ValueError
        if not isinstance(turn_count, int):
            raise ValueError
        if not isinstance(turn_since_last_placement, int):
            raise ValueError
        if not isinstance(score, int):
            raise ValueError
        self.nick_name = nick_name
        self.player_num = player_num
        self.turn_count = turn_count
        self.turn_since_last_placement = turn_since_last_placement
        self.score = score
        self.tile_array = [Tile()]
        self.last_placed_word = [] # (x,y) tuples of location on board
        self.skip_next_turn = False

    def tile_count(self) -> int:
        non_null_tiles = 0
        for t in self.tile_array:
            if t.is_tile():
                non_null_tiles += 1
        return non_null_tiles
