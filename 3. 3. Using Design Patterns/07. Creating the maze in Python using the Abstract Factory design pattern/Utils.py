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

from enum import Enum

class MapSite():
    def Enter(self):
        raise NotImplementedError("Abstract Base Class method")

class Direction(Enum):
    North = 0
    East  = 1
    South = 2
    West  = 3


# common code moved into function
def find_maze_rooms(maze_obj):  # pass object into function
    # find its rooms
    maze_rooms = []
    for room_number in range(5):
        try:
            #   get the room number
            room = maze_obj.RoomNo(room_number)
            print('\n^^^ Maze haz room: {}'.format(room_number, room))
            print('    Entering the room...')
            room.Enter()
            # append rooms to list
            maze_rooms.append(room)
            for idx in range(4):
                side = room.GetSide(idx)
                side_str = str(side.__class__).replace("<class '__main__.", "").replace("'>", "")
                print('    Room: {}, {:<15s}, Type: {}'.format(room_number, Direction(idx), side_str))
                print('    Trying to enter: ', Direction(idx))
                side.Enter()
                if 'Door' in side_str:
                    door = side
                    if not door._isOpen:
                        print('   ***Opening the door...')
                        door._isOpen = True
                        door.Enter()
                    print('\t', door)
                    #   get the room on other side of the door
                    other_room = door.OtherSideFrom(room)
                    print('\tOn the other side of the door is Room: {}\n'.format(other_room._roomNumber))
        except KeyError:
            print('No room', room_number)
    num_of_rooms = len(maze_rooms)
    print('\nThere are {} rooms in the Maze.'.format(num_of_rooms))
    print('Both doors are the same object and they are on the East and West side of the two rooms.')

    ###################################################################################################################