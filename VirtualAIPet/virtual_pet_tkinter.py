# virtual_pet_tkinter.py
import tkinter as tk
from tkinter import ttk
from virtual_pet import VirtualPet
import random

class VirtualPetTkinterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Pet")
        self.geometry("300x200")

        self.pet = VirtualPet("Pet")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Virtual Pet", font=("Arial", 16)).pack(pady=10)

        self.status_label = ttk.Label(self, text="")
        self.status_label.pack(pady=5)
        self.update_status_label()

        action_frame = ttk.Frame(self)
        action_frame.pack(pady=10)

        ttk.Button(action_frame, text="Feed", command=self.feed_pet).grid(row=0, column=0, padx=5)
        ttk.Button(action_frame, text="Play", command=self.play_pet).grid(row=0, column=1, padx=5)
        ttk.Button(action_frame, text="Rest", command=self.rest_pet).grid(row=0, column=2, padx=5)

    def feed_pet(self):
        food_amount = random.randint(5, 15)
        self.pet.feed(food_amount)
        self.update_status_label()

    def play_pet(self):
        play_time = random.randint(5, 15)
        self.pet.play(play_time)
        self.update_status_label()

    def rest_pet(self):
        rest_time = random.randint(5, 15)
        self.pet.rest(rest_time)
        self.update_status_label()

    def update_status_label(self):
        status = f"""Hunger: {self.pet.hunger}
Happiness: {self.pet.happiness}
Energy: {self.pet.energy}"""
        self.status_label.config(text=status)

def run_tkinter_app():
    app = VirtualPetTkinterApp()
    app.mainloop()
