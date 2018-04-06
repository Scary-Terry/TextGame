#Sam Ruchti
#Text Adventure
#4/3/18

class Creatures:

    def __init__(self, name):
        self.name = name

    def health(self, health):
        self.health = health


class Hostile_Monster(Creatures):
    """"""



print("You wake up in a daze, you don't recognize your surroundings."
      "What do you decide to do?")

x = input("1) Explore and get familiar with your surroundings.\n"
          "2) Stay where you are and see what happens.\n"
              "3) Stay in the area and wait for civilization to come to you.\n")
if x.find("1") >= 0:
    print("You decided to explore, but you encountered a Hostile Enemy and"
          "died")
    h = Hostile_Monster('Enemy')
    h.health(100)

if x.find("2") >= 0:
    print("You are safe...for now")
    print 
if x.find("3") >= 0:
    print("It has been a substantial amount of time...no one has come"
          "you'll die if you dont do something soon.")
