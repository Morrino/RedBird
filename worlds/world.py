#import numpy;
import random;

from rooms.room import Room

class World:

  def __init__(selfie, description='an empty world, very sad'):
    selfie.description = description
    selfie.start = None # room

class RandomWorld:
  """
  Matrix style indexing?
  or
  x is horizontal (index of width)
  y is vertical   (index of height)
  """

  def _debug_world_1(selfie):
    for y in range(selfie.height):
      for x in range(selfie.width):
        print(f'{y},{x} = {selfie.world[y][x].description}')
        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2

  def __init__(selfie, description='a randomly generated world', w=5, h=8):
    selfie.description = description
    selfie.width = w
    selfie.height = h
    selfie.density = 0.5
    selfie.freedom = 0.8

    selfie.world = [[Room(f'a room at {y},{x}') for x in range(w)] for y in range(h)]

    #selfie._debug_world_1()

    # create links between rooms
    for y in range(selfie.height):
      for x in range(selfie.width):
        try:
          assert y-1 >= 0
          selfie.world[y][x].north = selfie.world[y-1][x]
        except:
          pass # world limit
        try:
          selfie.world[y][x].south = selfie.world[y+1][x]
        except:
          pass # world limit
        try:
          selfie.world[y][x].east = selfie.world[y][x+1]
        except:
          pass # world limit
        try:
          assert x-1 >= 0
          selfie.world[y][x].west = selfie.world[y][x-1]
        except:
          pass # world limit

    # start in a random room on this world
    flat_world = [j for i in selfie.world for j in i]
    selfie.start = random.choice(flat_world)
