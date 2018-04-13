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

print ("To restart the game, type adv() and hit enter at anytime.")
def adv():
    print("You wake up in a daze, you don't recognize your surroundings.\n"
          "What do you decide to do?")
    print("")
    x = input("1) Explore and get familiar with your surroundings.\n"
              "2) Stay where you are and see what happens.\n"
              "3) Stay in the area and wait for civilization to come to you.\n")
    print("")
    if x.find("1") >= 0:
        print("You decided to explore, but you encountered a Hostile Enemy and "
              "died")
        h = Hostile_Monster("Enemy")
        print (h)
        

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
                print("You now have food and water to last you tonight and "
                      "tomorrow\n"
                      "but you did not make it to the next day...You died in your sleep")
            if x.find("4") >= 0:
                print("You found some colored fishing line in your pocket and a "
                      "bendable stick, so you make a bow\n"
                      "there's just one problem\n"
                      "...Arrows\n")
                def arm():
                    print("A bow is no good without arrows.")
                    x = input("How will you aquire these arrows?\n"
                              "1) Craft your own arrows\n"
                              "2) The island is abandoned, you find some "
                              "in the grass\n"
                              "3) Search to see if you could steal some from people\n")
                    
                    if x.find('1') >= 0:
                        print ("You couldn't find any sticks fit for arrows...you were defenseless"
                               "to an attack and you died")
                    if x.find('2') >= 0:
                        arrows = 3
                        print ("You have found 3 arrows but they won't last long")
                        def fight():
                            x = input('')
                    if x.find('3') >= 0:
                        print ("You went searching and didn't encouter anyone...soon after you return to your temperary home, you are ambushed "
                               "and cannot defend yourself")
                arm()
        stay_put()
    if x.find("3") >= 0:
        print("It has been a substantial amount of time...no one has come,\n"
              "You'll die if you don't do something soon.")
        def desperate():
            print("What do you choose to get first?")
            x = input("1) Food\n"
                      "2) Water\n"
                      "3) Shelter\n"
                      "4) Warmth\n")
            if x.find("1") >= 0:
                print("You have food for a substantial amount of time but you are"
                      "in danger of losing your life from the lack of the other "
                      "necessities of life")
            if x.find("2") >= 0:
                print("You are now hydrated, but you die from a sickness"
                      "because the water was not filtered")
            if x.find("3") >= 0:
                print("You are safe from the harm of the weather")
            if x.find("4") >= 0:
                print("You are have successfully made a fire during"
                      "the cold of night but you are starving")
        desperate()


adv()
