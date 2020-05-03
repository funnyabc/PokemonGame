
from enum import Enum
import string

class Type(Enum):
    FIRE = 1
    WATER = 2
    GRASS = 3
    ELECTRIC = 4

class Pokemon:
    def __init__(self, p_type, level, name):
        self.type = p_type
        self.level = level
        self.name = name
        self.health = 100
        self.max_health = level * 20
        self.exp_points = 0
        self.is_knocked_out = False
        self.moves = []

    def __repr__(self):
        return "{} Type: {}".format(self.name, self.type)


    def lose_health(self, loss):
        if self.health - loss <= 0:
            self.health = 0
            self.knock_out()
        else:
            self.health -= loss
        print("{} now has {} health.".format(self.name, self.health))
        

    def gain_health(self, gain):
        if self.health == 0:
            self.revive()
        self.health = min(self.max_health, self.health + gain)
        print("{} now has {} health.".format(self.name, self.health))


    def knock_out(self):
        self.is_knocked_out = True
        print("{} is knocked out.".format(self.name))


    def revive(self):
        self.is_knocked_out = False
        print("{} has been revived.".format(self.name))


    def add_move(self, move, damage):
        if len(self.moves) == 4:
            replace = input("Only 4 moves allowed per Pokémon. Would you like to replace one? (y/n)")
            if replace.lower()[0] == 'y':
                for i, skill in enumerate(self.moves):
                    print("{}: {}".format(i, skill))
                selection = input("Choose the number corresponding to the move you want to replace.")
                if selection in set(string.digits):
                    self.moves[int(selection)] = (move, damage)
            else:
                print("Not adding move.")
        else:
            self.moves.append((move, damage))

    def attack(self, opponent):
        if self.is_knocked_out:
            print("{} is knocked out. Please choose another Pokemon".format(self.name))
            return
        damage = 10
        if self.type != opponent.type:
            if self.type == Type.FIRE:
                if opponent.type == Type.GRASS:
                    damage *= 2
                else:
                    damage /= 2
            elif self.type == Type.GRASS:
                if opponent.type == Type.WATER:
                    damage *= 2
                else:
                    damage /= 2
            elif self.type == Type.WATER:
                if opponent.type == Type.FIRE:
                    damage *= 2
                else:
                    damage /= 2
        opponent.lose_health(damage)
        print("Dealt {} damage to opponent's {}".format(damage, opponent.name))
        


class Trainer:
    def __init__(self, name):
        self.name = name
        self.potions = []
        self.pokemons = []
        self.current_pokemon = 0
        
    def use_potion(self):
        if self.potions:
            potion = self.potions.pop(0)
            self.pokemons[self.current_pokemon].gain_health(potion)
        else:
            print("No potions available")

    def attack(self, opponent):
        current_pokemon = self.pokemons[self.current_pokemon]
        opponent_pokemon = opponent.pokemons[opponent.current_pokemon]
        current_pokemon.attack(opponent_pokemon)

    def switch_pokemon(self, num):
        if num >= len(self.pokemons):
            print("invalid selection")
            return
        else:
            if self.pokemons[num].is_knocked_out:
                print("{} is knocked out. Please select another pokemon.".format(self.pokemons[num].name))
                return
            self.current_pokemon = num
            print("Current active pokemon: {}".format(self.pokemons[self.current_pokemon].name))
    
    def add_pokemon(self, pokemon):
        if len(self.pokemons) == 6:
            print("Max number of pokemon reached. Would you like to replace one")
        else:
            self.pokemons.append(pokemon)
            print("{} now available to use.".format(pokemon.name))

    def available_pokemon(self):
        for p in self.pokemons:
            print(p)