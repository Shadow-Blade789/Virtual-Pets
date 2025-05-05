import random

class Pet():
    def __init__(self, name, age, hunger, boredom, sleepiness):
        self.dead = False; self.name = name; self.age = age; self.hunger = hunger; self.boredom = boredom; self.sleepiness = sleepiness
    def Feed(self):
        if self.dead == False:
            self.hunger -= 3
            if self.hunger < 0:
                self.hunger = 0
            print(f"{self.name} has been fed. Hunger is now {self.hunger}.")
        else:
            print(f"{self.name} is dead and cannot be fed.")
    def Play(self):
        if self.dead == False:
            self.boredom -= 3
            if self.boredom < 0:
                self.boredom = 0
            print(f"{self.name} has played. Boredom is now {self.boredom}.")
        else:
            print(f"{self.name} is dead and cannot play.")
    def Sleep(self):
        if self.dead == False:
            self.sleepiness -= 5
            if self.sleepiness < 0:
                self.sleepiness = 0
            print(f"{self.name} has slept. Sleepiness is now {self.sleepiness}.")
        else:
            print(f"{self.name} is dead and cannot sleep.")
    def Wait(self):
        if self.dead == False:
            self.age += 1
            self.hunger += 1
            if self.hunger > 10:
                self.hunger = 10
            self.boredom += 1
            if self.boredom > 10:
                self.boredom = 10
            self.sleepiness += 1
            if self.sleepiness > 10:
                self.sleepiness = 10
            print(f"{self.name} has waited. Age is now {self.age}, Hunger is now {self.hunger}, Boredom is now {self.boredom}, Sleepiness is now {self.sleepiness}.")
        else:
            print(f"{self.name} is dead and cannot wait.")
    def check_death(self):
        if self.boredom >= 10 or self.sleepiness >= 10 or self.hunger >= 10 or self.age == random.randint(15, 20):
            self.dead = True
            print(f"{self.name} is dead.")
        else:
            print(f"{self.name} is alive.")
        
####----Task 1----####
#Set up your pet with the following attributes:
age = 0; hunger = 5; boredom = 3; sleepiness = 3

####----Task 2----####
Petoo_McShmetto = Pet("Petoo McShmetto", age, hunger, boredom, sleepiness)
e = input("What do yuo want to do?")
while e != "exit":
    if e == "feed":
        Petoo_McShmetto.Feed()
    elif e == "play":
        Petoo_McShmetto.Play()
    elif e == "sleep":
        Petoo_McShmetto.Sleep()
    elif e == "wait":
        Petoo_McShmetto.Wait()
    else:
        print("Invalid command.")
    Petoo_McShmetto.check_death()
    e = input("What do you want to do?")
####----Task 3----#### 

###----Task 4----####

####---Task 5----####
#make it so that the feed, sleep, play and wait will check if the pet
#is dead before you upadate those properties.

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)