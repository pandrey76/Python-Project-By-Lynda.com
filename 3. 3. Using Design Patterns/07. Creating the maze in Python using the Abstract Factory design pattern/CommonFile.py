#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     05.09.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#from MazeAbstractFactoryPattern import *
from MazeAbstructFactoryPattern_Enchanted import *
from MazeAbstractFactoryPattern_Bombed import *

def play_game(aFactory, num_of_stars=44, explode_bomb=False):
    print('\n')
    print('*' * num_of_stars)
    print('*** The Maze Game ***')
    print('*' * num_of_stars)

    factory = aFactory
    print(factory)
    print('=' * num_of_stars)

    maze_obj = MazeGame().CreateMaze(factory)
    find_maze_rooms(maze_obj)

    if explode_bomb:
        print('\n*** Bomb exploded - walls are damaged! ***')
        maze_obj._rooms[1].bomb_exploded = True
        for side in range(4):
            cur_side = maze_obj._rooms[1]._sides[side]
            if 'BombedWall' in str(cur_side):
                cur_side.wall_is_damaged = True
                print('Wall is damaged:', cur_side, cur_side.wall_is_damaged)


############################################
play_game(MazeFactory)  # pass in class directly
play_game(MazeFactory())  # pass in instance of class
play_game(EnchantedMazeFactory)
play_game(BombedMazeFactory)
play_game(BombedMazeFactory, explode_bomb=True)