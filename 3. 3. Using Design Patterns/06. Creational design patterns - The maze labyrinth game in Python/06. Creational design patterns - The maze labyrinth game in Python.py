﻿#!/usr/bin/env python
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


# * Introducing to Creational Design Patterns
# * The Design :
#                                                        __________
#                                                       |   Maze   |
#                |------------------------------------->|_________ |
#                |                                      |          |
#                |                                      | Enter()  |
#                |                                      |__________|
#                |                                           |
#                |                   |-----------------------^----------------------|
#                |                   |                       |                      |
#                | sides             |                       |                      |
#                |             ______|_____               ___|____             _____|______
#                |------------|   Room     |             |        |           |    Door    |
#                             |____________|             |  Wall  |           |____________|
#                             |            |             |________|           |            |
# ___________                 | Enter()    |             |        |           |  Enter()   |
#|   Maze    | rooms          | SetSide()  |             | Enter()|           |  isOpen    |
#|___________|                | GetSide()  |             |________|           |____________|
#|           |--------------->|____________|
#| AddRoom() |                | roomNumber |
#| RoomNo()  |                |____________|
#|___________|

# * Several ways to create. "Rooms"
