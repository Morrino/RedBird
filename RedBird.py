#!/usr/bin/env python3
# coding=utf-8

from rooms.room import Room

worlds = {
    '1': "Rain forest hipster",
    '2': "Steampunk underground township",
    '3': "Radiated misty city",
    '4': "Techno elitist planet",
    '5': "Blackout tunnel",
}


def worlds_string():
    return "\n".join([f"{k}: {v}" for k, v in worlds.items()])

def welcome_user():
    username = input("Please, enter your character's nickname for the game: \n")

    if not username:
        username = "Pepito"

    print(f"Welcome, {username}, to this very unique game called Red bird!")

    return username


def select_world(username):
    while True:
      try:
        print(f"Please, select a world to explore:\n")
        world = input(f"{worlds_string()}\n")

        assert world in worlds.keys(), 'Yoyo, choose a correct world, por favor!'
        print(f"You chose wisely, {username}. Be careful and look out for the red birds in {worlds[world]}.")
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
  room = Room('a room only leading north')
  room.north = Room('a room north of beginning')
  while True:
    try:
      print("")
      print(f'You are in a room in {worlds[welcome.world]}.')
      print(f"It's {room.description}.")
      answer = input(f"What do you do, {welcome.username}? ")
      if 'q' == answer:
        break
      elif 'go' in answer:
        if 'north' in answer:
          nextroom = room.north
        if 'south' in answer:
          nextroom = room.south
        if 'east' in answer:
          nextroom = room.east
        if 'west' in answer:
          nextroom = room.west
      assert nextroom is not None#, 'wat?'
      room = nextroom
    except:
      print("")
      print('wat?')
      continue
  print('See you soon!')
