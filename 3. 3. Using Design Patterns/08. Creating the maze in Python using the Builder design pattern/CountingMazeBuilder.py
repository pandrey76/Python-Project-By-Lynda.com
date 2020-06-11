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


from  MazeBuilderPattern import  *

# implementation
class CountingMazeBuilder(MazeBuilder):
    def __init__(self):
        self._rooms = 0
        self._doors = 0

    def BuildRoom(self, n):
        self._rooms += 1

    def BuildDoor(self, r1, r2):
        self._doors += 1

    def GetCounts(self):
        return self._rooms, self._doors

# ==================================================================
# Self-testing section
# ==================================================================
if __name__ == '__main__':

    print('\n' * 2)
    print('*' * 21)
    print('*** The Counting Maze Game ***')
    print('*' * 21)

    game = MazeGame()
    builder = CountingMazeBuilder()

    game.CreateMaze(builder)
    rooms, doors = builder.GetCounts()

    print('The maze has {} rooms and {} doors'.format(rooms, doors))
