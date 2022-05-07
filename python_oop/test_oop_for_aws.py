class Game:
    def __init__(self):
        self.name="Player1"
        self.stats=100
character=Game() #instance
print(character.name)
character.name="Player2"
character.isgood=True
print(character.name)
print(character.stats)
print(character.isgood)

"""inheritance"""

class Computer:
    number_of_pc = 0 #class attribute
    def __init__(self):
        self.name="My Computer"
        self.os="Windows 98"
        Computer.number_of_pc=Computer.number_of_pc+1
mylaptop = Computer()
pc1 = Computer()
pc2 = Computer()
pc3 = Computer()

print(Computer.number_of_pc)