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
class StandardMazeBuilder(MazeBuilder):

    def __init__(self):
        self._currentMaze = None            #   member to hold a Maze

    def BuildMaze(self):
        self._currentMaze = Maze()

    def BuildRoom(self, n):
        try:
            self._currentMaze.RoomNo(n)
        except:
            print( 'Room {} does not exist - building this room'.format((n)))
            room = Room(n)
            self._currentMaze.AddRoom(room)

            room.SetSide(Direction.North.value, Wall())     #   all sides a Walls
            room.SetSide(Direction.South.value, Wall())
            room.SetSide(Direction.East.value, Wall())
            room.SetSide(Direction.West.value, Wall())

    def BuildDoor(self, n1, n2):
        r1 = self._currentMaze.RoomNo(n1)
        r2 = self._currentMaze.RoomNo(n2)
        d = Door(r1, r2)

        r1.SetSide(self.CommonWall(r1, r2), d)      #   Door replaces Wall
        r2.SetSide(self.CommonWall(r2, r1), d)      #   Door replaces Wall

        print()
        for side in range(4):
            if 'Door' in str(r1._sides[side]):
                print ('Room1: ', r1._sides[side], Direction(side))
            if 'Door' in str(r2._sides[side]):
                print ('Room2: ', r2._sides[side], Direction(side))

    def GetMaze(self):
        return  self._currentMaze

    def CommonWall(self, aRoom, anotherRoom):
        # layout: room1, room2 etc. from left (West) to right (East)
        if aRoom._roomNumber < anotherRoom._roomNumber:
            return Direction.East.value
        else:
            return Direction.West.value

# ==================================================================
# Self-testing section
# ==================================================================
if __name__ == '__main__':
    print('*' * 21)
    print('*** The Maze Game ***')
    print('*' * 21)

    maze = Maze
    game = MazeGame()
    builder = StandardMazeBuilder()

    game.CreateMaze(builder)
    maze = builder.GetMaze()