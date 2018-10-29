#!/usr/bin/env python3
# coding=utf-8

from rooms.room import Room
from worlds.world import World

new_line = "\n"
worlds = {
    '1': "Rain Forest Hipster",
    '2': "Steampunk Underground Township",
    '3': "Radiated Misty City",
    '4': "Techno Elitist Planet",
    '5': "Blackout Tunnel",
}


def worlds_string():
    return new_line.join([f"{key}: {value}" for key, value in worlds.items()])

def welcome_user():
    username = input(f"Please, enter your character's nickname for the game: {new_line}")

    if not username:
        username = "Pepito"

    print(f"Welcome, {username}, to this very unique game called Red bird!")

    return username


def select_world(username):
    while True:
      try:
        print(f"Please, select a world to explore:{new_line}")
        world = input(f"{worlds_string()}{new_line}")

        assert world in worlds.keys(), 'Yoyo, choose a correct world, por favor!'
        print(f"{new_line}You chose wisely, {username}. Be careful and look out for the red birds in {worlds[world]}.")
        input()
      except:
        continue
      break
    return world


class WelcomeToRedBirdGame:
    def __init__(self):
      self.username = welcome_user()
      self.world = select_world(self.username)

if __name__ == '__main__':
  welcome = WelcomeToRedBirdGame()
  #welcome.username
  #welcome.world

  world = World(worlds[welcome.world])
  world.start = Room('a room only leading north')
  world.start.north = Room('a room north of beginning')

  room = world.start
  while True:
    try:
      print("")
      print(f'You are in a room in {world.description}.')
      print(f"It's {room.description}.")
      answer = input(f"What do you do, {welcome.username}? ").lower()
      if 'q' or 'quit'  == answer:
        break
      elif 'go' in answer:
        if 'north' in answer:
          nextroom = room.north
          nextroom.south = room
        if 'south' in answer:
          nextroom = room.south
          nextroom.north = room
        if 'east' in answer:
          nextroom = room.east
          nextroom.west = room
        if 'west' in answer:
          nextroom = room.west
          nextroom.east = room
      assert nextroom is not None#, 'wat?'
      room = nextroom
      nextroom = None

    except:
      print("")
      print('wat?')
      continue
  print('See you soon!')
