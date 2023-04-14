import random
import time

# virtual_pet.py
import random

class VirtualPet:
    def __init__(self, name, hunger=50, happiness=50, energy=50):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def feed(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0

    def play(self, duration):
        self.happiness += duration
        self.energy -= duration
        self.hunger += duration // 2
        if self.happiness > 100:
            self.happiness = 100
        if self.energy < 0:
            self.energy = 0

    def rest(self, duration):
        self.energy += duration
        self.hunger += duration // 2
        if self.energy > 100:
            self.energy = 100

    def __str__(self):
        return f"""{self.name}:
            Hunger: {self.hunger}
            Happiness: {self.happiness}
            Energy: {self.energy}"""


'''
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self, food_amount):
        self.hunger -= food_amount
        if self.hunger < 0:
            self.hunger = 0
        print(f"You fed {self.name}. Hunger is now {self.hunger}.")

    def play(self, play_time):
        if self.energy >= play_time:
            self.happiness += play_time
            self.energy -= play_time
            if self.happiness > 100:
                self.happiness = 100
            print(f"You played with {self.name}. Happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is too tired to play.")

    def rest(self, rest_time):
        self.energy += rest_time
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} rested. Energy is now {self.energy}.")

    def show_status(self):
        print(f"{self.name}'s status:")
        print(f"  Hunger: {self.hunger}")
        print(f"  Happiness: {self.happiness}")
        print(f"  Energy: {self.energy}")


def main():
    pet_name = input("Enter your pet's name: ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nChoose an action:")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Check status")
        print("5. Exit")
        
        action = input("Enter the number of the action: ")

        if action == "1":
            food_amount = random.randint(5, 15)
            pet.feed(food_amount)
        elif action == "2":
            play_time = random.randint(5, 15)
            pet.play(play_time)
        elif action == "3":
            rest_time = random.randint(5, 15)
            pet.rest(rest_time)
        elif action == "4":
            pet.show_status()
        elif action == "5":
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Invalid input. Please choose a valid action.")

        time.sleep(1)

if __name__ == "__main__":
    main()
'''