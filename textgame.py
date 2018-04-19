"""
    Sam Ruchti
    Text Adventure
    4/3/18
"""
import time

class Creatures:

    def __init__(self, name):
        self.name = name

    def health(self, health):
        self.health = health


class Hostile_Monster(Creatures):
     """"""

print ('To restart the game, type "restart" and hit enter at anytime.\n'
       "To quit the game type quit and hit enter.\n")

    
def adv():

    
    s = ("You wake up in a daze, you don't recognize your surroundings.\n"
         "What do you decide to do?")
    for letter in s:
        print(letter, end='')
        time.sleep(.1)
    print('')

    print("")
    x = input("1) Explore and get familiar with your surroundings.\n"
              "2) Stay where you are and see what happens.\n"
              "3) Stay in the area and wait for civilization to come to you.\n")
    if x.find("restart") >= 0:
        s = "You have chosen the easy way out"
        for letter in s:
            print(letter, end='')
            time.sleep(.1)
        print('')
        s = "You will be revived when the progress bar is complete"
        for letter in s:
            print(letter, end='')
            time.sleep(.1)
        print('')
        s = "[=======================================================]"
        for letter in s:
            print(letter, end='')
            time.sleep(.5)
        print('')
        adv()

    if x.find("quit") >= 0:
        s = "You have chosen the easy way out"
        for letter in s:
            print(letter, end='')
            time.sleep(.1)
        print('')
        s = "You will be revived when the progress bar is complete"
        for letter in s:
            print(letter, end='')
            time.sleep(.1)
        print('')
        s = "[=======================================================]"
        for letter in s:
            print(letter, end='')
            time.sleep(.5)
        print('')

    print("")
    
    if x.find("1") >= 0:
        s = "You decided to explore, but you encountered a Hostile Enemy while unarmed."
        for letter in s:
            print(letter, end='')
            time.sleep(.1)
        print('')
        s = "You Have Died"
        for letter in s:
            print(letter, end='')
            time.sleep(.1)
        print('')
        s = "You will be revived when the progress bar is complete"
        for letter in s:
            print(letter, end='')
            time.sleep(.1)
        print('')
        s = "[=======================================================]"
        for letter in s:
            print(letter, end='')
            time.sleep(.5)
        print('')
        adv()
    
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
                s = ("Smart of you to wait for Nightfall, but it didnt help you"
                     " too much.\n")
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "You were killed because you were defenseless"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "You will be revived when the progress bar is complete"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "[=======================================================]"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.5)
                print('')
                adv()
                
            if x.find("2") >= 0:
                s = "Something found you in the night while you were sleeping/n You were Killed"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "You will be revived when the progress bar is complete"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "[=======================================================]"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.5)
                print('')
                adv()
                
            if x.find("3") >= 0:
                s = ("You now have food and water to last you tonight and "
                      "tomorrow\n"
                      "but you did not make it to the next day...You died in your sleep "
                      "mysteriously")
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "You will be revived when the progress bar is complete"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "[=======================================================]"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.5)
                print('')
                adv()
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
                        s = ("You couldn't find any sticks fit for arrows...you were defenseless"
                             "to an attack and you died")
                        for letter in s:
                            print(letter, end='')
                            time.sleep(.1)
                        print('')
                        s = "You will be revived when the progress bar is complete"
                        for letter in s:
                            print(letter, end='')
                            time.sleep(.1)
                        print('')
                        s = "[=======================================================]"
                        for letter in s:
                            print(letter, end='')
                            time.sleep(.5)
                        print('')
                        adv()
                    if x.find('2') >= 0:
                        arrows = 3
                        s = ("You have found 3 arrows but they won't last long"
                             'Now that you have arrows, What will you do now?\n')
                        x = input('1) Get familiar with your surroundings'
                                  '2) Stay put and defend yourself'
                                  '3) Go hunting')
                        if x.find('1') >= 0:
                            s = ("
                    if x.find('3') >= 0:
                        s = ("You went searching and didn't encouter anyone...soon after you return to your temperary home, you are ambushed "
                             "and cannot defend yourself")
                        for letter in s:
                            print(letter, end='')
                            time.sleep(.1)
                        print('')
                        s = "You will be revived when the progress bar is complete"
                        for letter in s:
                            print(letter, end='')
                            time.sleep(.1)
                        print('')
                        s = "[=======================================================]"
                        for letter in s:
                            print(letter, end='')
                            time.sleep(.5)
                        print('')
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
                print("You have food for a substantial amount of time but you "
                      "losed your life from the lack of the other "
                      "necessities of life")
            if x.find("2") >= 0:
                s = ("You are now hydrated, but you die from a sickness"
                     "because the water was not filtered")
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "You will be revived when the progress bar is complete"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "[=======================================================]"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.5)
                print('')
            if x.find("3") >= 0:
                s = ("You are safe from the harm of the weather\n"
                     "What next?")
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                x = input("1) Food\n"
                          "2) Water\n"
                          "3) Warmth\n")
                if x.find("1") >= 0:
                    s = ("You now are able to survive a little while longer")
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    time.sleep(1)
                    s = ("But it turns out that the berries that you gathered"
                         "were poison berries, and they killed you")
                    for letter in s:
                        print (letter, end='')
                        time.sleep(.1)
                    print('')
                    s = "You will be revived when the progress bar is complete"
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    s = "[=======================================================]"
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.5)
                    print('')
                    adv()

                if x.find("2") >= 0:
                    s = ("You currently arent dying, so i guess thats good")
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    time.sleep(3)
                    s = "Wait"
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    time.sleep(1.5)
                    s = ("Something just came out of the woods next to you, "
                         "its a rabid bear\n"
                         "You try to run but it is too fast and catches you, "
                         "You were Killed")
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    s = "You will be revived when the progress bar is complete"
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    s = "[=======================================================]"
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.5)
                    print('')
                    adv()
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.5)
                    print('')
                    
                if x.find("3") >= 0:
                    s = ("You are beginning to Hallucinate, You pass out "
                         "and die from dehydration")
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    s = "You will be revived when the progress bar is complete"
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.1)
                    print('')
                    s = "[=======================================================]"
                    for letter in s:
                        print(letter, end='')
                        time.sleep(.5)
                    print('')
                    adv()
            if x.find("4") >= 0:
                s = ("You are have successfully made a fire during"
                     "the cold of night")
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                time.sleep(1)
                s = ("But the light and smoke attracted hostiles and you were killed")
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "You will be revived when the progress bar is complete"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.1)
                print('')
                s = "[=======================================================]"
                for letter in s:
                    print(letter, end='')
                    time.sleep(.5)
                print('')
                adv()
        desperate()


adv()
