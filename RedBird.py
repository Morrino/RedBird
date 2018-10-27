#!/usr/bin/env python3
# coding=utf-8

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
    print(f"Please, select a world to explore:\n")
    world = input(f"{worlds_string()}\n")
    print(f"You chose wisely, {username}. Be careful and look out for the red birds in {worlds[world]}.")


class WelcomeToRedBirdGame:
    username = welcome_user()
    select_world(username)
