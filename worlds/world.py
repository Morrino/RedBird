#import numpy;

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
        print(f'{x},{y} = {selfie.world[y][x].description}')

  def __init__(selfie, description='a randomly generated world', w=5, h=8):
    selfie.description = description
    selfie.width = w
    selfie.height = h
    selfie.density = 0.5
    selfie.freedom = 0.8

    selfie.world = [[Room(f'This room is at {x},{y}') for x in range(w)] for y in range(h)]

    #selfie._debug_world_1()

    # get a list of existing rooms and choice one
    # flatten world and choice
    selfie.start = selfie.world[0][0]
