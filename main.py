import csv
import random

class Pet():
    def __init__(self, name, age, hunger, boredom, sleepiness):
        self._Pet__private_dead = False; self._Pet__private_name = name; self._Pet__private_age = age; self._Pet__private_hunger = hunger; self._Pet__private_boredom = boredom; self._Pet__private_sleepiness = sleepiness; self._Pet__private_art1 = "  / \__\n (    @\___\n /         O\n/   (_____/\n/_____/ U\n"; self._Pet__private_art2 = "   /^ ^\\n  / 0 0 \ \n /   Y   \\n V\__|__/V\n   /   \\n  ||___||\n (__/ \__)"; self._Pet__private_art3 = r = '''    ___
 __/_  `.  .-"""-.
 \_,` | \-'  /   )`-')
  "") `"`    \  ((`"`
 ___Y  ,    .'7 /|
(_,___/...-` (_/_/
'''
    def Feed(self):
        if self._Pet__private_dead == False:
            self._Pet__private_hunger -= 3
            if self._Pet__private_hunger < 0:
                self._Pet__private_hunger = 0
            print(f"{self._Pet__private_name} has been fed. Hunger is now {self._Pet__private_hunger}.")
        else:
            print(f"{self._Pet__private_name} is dead and cannot be fed.")
    def Play(self):
        if self._Pet__private_dead == False:
            self._Pet__private_boredom -= 3
            if self._Pet__private_boredom < 0:
                self._Pet__private_boredom = 0
            print(f"{self._Pet__private_name} has played. Boredom is now {self._Pet__private_boredom}.")
        else:
            print(f"{self._Pet__private_name} is dead and cannot play.")
    def Sleep(self):
        if self._Pet__private_dead == False:
            self._Pet__private_sleepiness -= 5
            if self._Pet__private_sleepiness < 0:
                self._Pet__private_sleepiness = 0
            print(f"{self._Pet__private_name} has slept. Sleepiness is now {self._Pet__private_sleepiness}.")
        else:
            print(f"{self._Pet__private_name} is dead and cannot sleep.")
    def Wait(self):
        if self._Pet__private_dead == False:
            self._Pet__private_age += 1
            self._Pet__private_hunger += 1
            if self._Pet__private_hunger > 10:
                self._Pet__private_hunger = 10
            self._Pet__private_boredom += 1
            if self._Pet__private_boredom > 10:
                self._Pet__private_boredom = 10
            self._Pet__private_sleepiness += 1
            if self._Pet__private_sleepiness > 10:
                self._Pet__private_sleepiness = 10
            print(f"{self._Pet__private_name} has waited. Age is now {self._Pet__private_age}, Hunger is now {self._Pet__private_hunger}, Boredom is now {self._Pet__private_boredom}, Sleepiness is now {self._Pet__private_sleepiness}.")
        else:
            print(f"{self._Pet__private_name} is dead and cannot wait.")
    def check_death(self):
        if self._Pet__private_boredom >= 10 or self._Pet__private_sleepiness >= 10 or self._Pet__private_hunger >= 10 or self._Pet__private_age == random.randint(15, 20):
            self._Pet__private_dead = True
            print(f"{self._Pet__private_name} is dead.")
        else:
            print(f"{self._Pet__private_name} is alive.")
    def __str__(self):
        return f"Pet Name: {self._Pet__private_name}, Age: {self._Pet__private_age}, Hunger: {self._Pet__private_hunger}, Boredom: {self._Pet__private_boredom}, Sleepiness: {self._Pet__private_sleepiness}, Dead: {self._Pet__private_dead}"
    def Checkart(self):
        if self._Pet__private_age <= 5:
            print(self._Pet__private_art1)
        elif self._Pet__private_age > 5 and self._Pet__private_age <= 10:
            print(self._Pet__private_art2)
        elif self._Pet__private_age > 10:
            print(self._Pet__private_art3)
    def Evolution(self):
        with open('evolutions.csv', 'r') as file:
            reader = csv.reader(file)
            evolutions = [row[0] for row in reader]
        random_evolution = random.choice(evolutions)
        while random_evolution == 1:
            random_evolution = random.choice(evolutions)
        print(f"Random evolution: {random_evolution}")
        name = random_evolution[1]; Type_1 = random_evolution[2]; Type_2 = random_evolution[3]; Hp = random_evolution[5]; Attack,Defense,Sp_Atk,Sp_Def,Speed,Generation,Legendary = random_evolution[6],random_evolution[7],random_evolution[8],random_evolution[9],random_evolution[10],random_evolution[11],random_evolution[12]
        self._Pet__private_name = f"{random_evolution}" + self._Pet__private_name

        print(f"Random evolution: {name}")
        self._Pet__private_name = f"{name}" + self._Pet__private_name
        print(f"New name: {self._Pet__private_name}")
        print(f"New Attack: {Attack}")
        print(f"New Defense: {Defense}")
        print(f"New Special Attack: {Sp_Atk}")
        print(f"New Special Defense: {Sp_Def}")
        print(f"New Speed: {Speed}")
        print(f"New Generation: {Generation}")
        print(f"New Legendary: {Legendary}")
        print(f"New Type_1: {Type_1}")
        print(f"New Type_2: {Type_2}")
        print(f"New Hp: {Hp}")
####----Task 1----####
#how can i access the second column of a line in the csv file evolutions.csv?

#Set up your pet with the following attributes:
age = 0; hunger = 5; boredom = 3; sleepiness = 3

####----Task 2----####
Petoo_McShmetto = Pet("Petoo McShmetto", age, hunger, boredom, sleepiness)
e = input("What do you want to do? (Feed, Play, Sleep, Wait, exit)")
while e != "exit":
    if e.lower() == "feed":
        Petoo_McShmetto.Checkart()
        Petoo_McShmetto.Feed()
    elif e.lower() == "play":
        Petoo_McShmetto.Checkart()
        Petoo_McShmetto.Play()
    elif e.lower() == "sleep":
        Petoo_McShmetto.Checkart()
        Petoo_McShmetto.Sleep()
    elif e.lower() == "wait":
        Petoo_McShmetto.Checkart()
        Petoo_McShmetto.Wait()
    elif e.lower() == "evolution":
        Petoo_McShmetto.Evolution()
    else:
        print("Invalid command.")
    Petoo_McShmetto.check_death()
    e = input("What do you want to do?")
####----Task 3----#### 

###----Task 4----####

####---Task 5----####
#make it so that the feed, sleep, play and wait will check if the pet
#is dead before you update those properties.



####---Task 6----####
#Use Python's predefined __str__ method to produce a string output
#for your pet. refer to page 4 of the tutorial if you don't know
#what I'm talking about.
#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)