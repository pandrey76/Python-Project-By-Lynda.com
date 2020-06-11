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

from MazeAbstractFactoryPattern import *

# Extend MazeFactory
class BombedMazeFactory(MazeFactory):
    @classmethod  # decorator
    def MakeWall(cls):
        return BombedWall()

    @classmethod  # decorator
    def MakeRoom(cls, n):  # n = roomNumber
        return RoomWithABomb(n)  # pass in roomNo, create a spell


class BombedWall(Wall):
    def __init__(self):
        self.wall_is_damaged = False  # True if bomb exploded


class RoomWithABomb(Room):
    def __init__(self, roomNo):
        super(RoomWithABomb, self).__init__(roomNo)
        self.has_bomb = True
        self.bomb_exploded = False

if __name__ == "__main__":

    num_of_stars = 44

    print('\n')
    print('*' * num_of_stars)
    print('*** The Maze Game ***')
    print('*' * num_of_stars)

    factory = BombedMazeFactory
    print(factory)
    print('=' * num_of_stars)

    maze_obj = MazeGame().CreateMaze(factory)
    find_maze_rooms(maze_obj)

    print('\n*** Bomb exploded - walls are damaged! ***')
    maze_obj._rooms[1].bomb_exploded = True
    for side in range(4):
        cur_side = maze_obj._rooms[1]._sides[side]
        if 'BombedWall' in str(cur_side):
            cur_side.wall_is_damaged = True
            print('Wall is damaged:', cur_side, cur_side.wall_is_damaged)
