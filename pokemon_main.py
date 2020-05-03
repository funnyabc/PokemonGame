from pokemon import *

if __name__ == "__main__":
    Ash = Trainer("Ash")
    Bulbasaur = Pokemon(Type.GRASS, 1, "Bulbasaur")
    Bulbasaur.add_move("whip", 10)
    Bulbasaur.add_move("leaf throw", 5)
    Bulbasaur.add_move("hit", 5)
    Bulbasaur.add_move("blossom", 20)
    print(Bulbasaur.moves)
    Bulbasaur.add_move("sprout", 30)
    print(Bulbasaur.moves)
    Misty = Trainer("Misty")
    Squirtle = Pokemon(Type.WATER, 1, "Squirtle")
    Ash.add_pokemon(Bulbasaur)
    Ash.available_pokemon()
    Misty.add_pokemon(Squirtle)
    Ash.attack(Misty)