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
  def __init__(selfie, description='a randomly generated world', w=5, h=8):
    selfie.description = description
    selfie.density = 0.5
    selfie.freedom = 0.8

    world = [[Room(f'This room is at {x},{y}') for x in range(w)] for y in range(h)]

    # print world
    for y in range(h):
      for x in range(w):
        print(f'{x},{y} = {world[y][x].description}')

    # get a list of existing rooms and choice one
    # flatten world and choice
    selfie.start = world[0][0]
