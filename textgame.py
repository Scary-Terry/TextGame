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


def adv():
    print("You wake up in a daze, you don't recognize your surroundings.\n"
          "What do you decide to do?")
    print("")
    x = input("1) Explore and get familiar with your surroundings.\n"
              "2) Stay where you are and see what happens.\n"
              "3) Stay in the area and wait for civilization to come to you.\n")
    print("")
    if x.find("1") >= 0:
        print("You decided to explore, but you encountered a Hostile Enemy and"
              "died")
        h = Hostile_Monster('Enemy')
        h.health(100)

    if x.find("2") >= 0:
        print("You are safe...for now")
        print("")
        def stay_put():
            print("It is now getting dark. What is your next move?")
            x = input("1) Wait until nightfall comes so you can move in darkness and be "
                  "concealed\n"
                  "2) Find a place to spend the night\n"
                  "3) Find a source of food and water\n"
                  "4) Find materials for weapons\n")
        
            if x.find("1") >= 0:
                print("Smart of you to wait for Nightfall, but it didnt help you"
                      " too much.\n"
                      "You died because you were defenseless.")
            if x.find("2") >= 0:
                print("Something found you in the night while you were sleeping/n"
                      "You were Killed")
            if x.find("3") >= 0:
                print("You now have food and water to last you tonight and"
                      "tomorrow")
            if x.find("4") >= 0:
                print("You found some colored fishing line in your pocket and a "
                      "bendable stick, so you make a bow\n"
                      "there's just one problem\n"
                      "...Arrows")
        stay_put()
    if x.find("3") >= 0:
        print("It has been a substantial amount of time...no one has come,\n"
              "You'll die if you don't do something soon.")
        def deperate():
            print("What do you think is the most important to survival?")
            x = input("1) Food\n"
                      "2) Water\n"
                      "3) Shelter\n"
                      "4) Warmth\n")
            if x.find("1") >= 0:
                print("")
            if x.find("2") >= 0:
                print("")
            if x.find("3") >= 0:
                print("")
            if x.find("4") >= 0:
                print("")



adv()
