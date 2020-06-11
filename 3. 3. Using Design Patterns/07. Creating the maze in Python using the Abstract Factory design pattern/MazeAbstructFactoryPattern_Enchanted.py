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
class EnchantedMazeFactory(MazeFactory):
    @classmethod  # decorator
    def MakeRoom(cls, n):  # n = roomNumber
        return EnchantedRoom(n, cls.CastSpell())  # pass in roomNo, create a spell

    @classmethod  # decorator
    def MakeDoor(cls, r1, r2):  # r1, r2 = two rooms
        return DoorNeedingSpell(r1, r2)  # door between rooms

    @classmethod
    def CastSpell(cls):
        return Spell()


class EnchantedRoom(Room):
    def __init__(self, roomNo, aSpell):
        super(EnchantedRoom, self).__init__(roomNo)
        print('The spell is: ', aSpell)


class Spell():
    def __repr__(self):  # overwrite string representation
        return '"A hard-coded spell"'


class DoorNeedingSpell(Door):
    def __init__(self, r1, r2):
        super(DoorNeedingSpell, self).__init__(r1, r2)
        self.spell = Spell()

    def Enter(self):
        print('    + This door needs a Spell...', self.spell)
        if self._isOpen:
            print('    **** You have passed through this door...')
        else:
            print('    ** This door needs to be opened before you can pass through it...')


if __name__ == '__main__':
    num_of_stars = 44
#    print('*' * num_of_stars)
#    print('*** The Maze Game - MazeFactory ***')
#    print('*' * num_of_stars)

    # creating the original Maze passing it in as a Factory
#    factory = MazeFactory  # pass in class directly
    #     factory = MazeFactory()     # pass in instance of class; no __init__(self)
#    print(factory)
#    print('=' * num_of_stars)

#    maze_obj = MazeGame().CreateMaze(factory)
#    find_maze_rooms(maze_obj)

    print('\n')
    print('*' * num_of_stars)
    print('*** The Maze Game - EnchantedMazeFactory ***')
    print('*' * num_of_stars)

    ############################################

    factory = EnchantedMazeFactory
    print(factory)
    print('=' * num_of_stars)

    maze_obj = MazeGame().CreateMaze(factory)
    find_maze_rooms(maze_obj)