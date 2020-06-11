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

from Utils import *

class Room(MapSite):

    def __init__(self, roomNo):
        self._sides = [MapSite] *4
        self._roomNumber = int(roomNo)

    def GetSide(self,Direction):
        return self._sides[Direction]

    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite

    def Enter(self):
        print( '    You have entered room: ' + str(self._roomNumber))

class Wall(MapSite):

    def Enter(self):
        print("         * You just run into Wall...")

class Door(MapSite):
    def __init__(self, Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False

    def OtherSideFrom(self, Room):
        print('\tDoor obj: This door is a side of Room: {}'.format(Room._roomNumber))
        if 1 == Room._roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1
        return other_room

    def Enter(self):
        if self._isOpen :
            print( '      **** You have passed through this door...' )
        else :
            print( '      ** This door needs to be opened before you can pass through it...')

class Maze():

    def __init__(self):
        # dictionary to hold room_number, room_obj <key, value> pairs
        self._rooms = {}

    def AddRoom(self, room):
        #use roomNumber as lookup value to retrieve room object
        self._rooms[room._roomNumber] = room

    def RoomNo(self, room_number):
        return self._rooms[room_number]

class MazeFactory():

    @classmethod            #   decorator
    def MakeMaze(cls):      #   cls, not self
        return Maze()       #   return Maze instance

    @classmethod            #   decotator
    def MakeWall(cls):
        return Wall()

    @classmethod            #   decotator
    def MakeRoom(cls, n):   #   n = roomNumber
        return Room(n)

    @classmethod            #   decotator
    def MakeDoor(cls, r1, r2):
        return Door(r1, r2)

class MazeGame():

    #Abstruct Factory
    def CreateMaze(self, factory = MazeFactory):
        aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        aDoor = factory.MakeDoor(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)

        r1.SetSide(Direction.North.value, factory.MakeWall())
        r1.SetSide(Direction.East.value, aDoor)
        r1.SetSide(Direction.South.value, factory.MakeWall())
        r1.SetSide(Direction.West.value, factory.MakeWall())

        r2.SetSide(Direction(0).value, factory.MakeWall())
        r2.SetSide(Direction(1).value, factory.MakeWall())
        r2.SetSide(Direction(2).value, factory.MakeWall())
        r2.SetSide(Direction(3).value, aDoor)

        return aMaze


if __name__ == '__main__':

    print('*' * 21)
    print('*** The Maze Game ***')
    print('*' * 21)

    #   creating the original Maze passing it in as a Factory

    #Оба способа будут одинаково работать
    factory = MazeFactory       #   pass in class directly
    #factory = MazeFactory()     #   pass in instance of class

    print(factory)

    maze_obj = MazeGame().CreateMaze(factory)
    find_maze_rooms(maze_obj)

