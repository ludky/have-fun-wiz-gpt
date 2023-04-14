# virtual_pet_kivy.py
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from virtual_pet import VirtualPet

class VirtualPetKivyApp(App):
    # Same as before, replace "VirtualPetApp" with "VirtualPetKivyApp"
    def build(self):
        self.pet = VirtualPet("Pet")

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.title_label = Label(text="Virtual Pet", font_size=24)
        layout.add_widget(self.title_label)

        self.status_label = Label(text="", font_size=16)
        layout.add_widget(self.status_label)
        self.update_status_label()

        action_layout = BoxLayout(orientation="horizontal", spacing=10)

        feed_button = Button(text="Feed", on_press=self.feed_pet)
        action_layout.add_widget(feed_button)

        play_button = Button(text="Play", on_press=self.play_pet)
        action_layout.add_widget(play_button)

        rest_button = Button(text="Rest", on_press=self.rest_pet)
        action_layout.add_widget(rest_button)

        layout.add_widget(action_layout)

        return layout

    def feed_pet(self, instance):
        food_amount = random.randint(5, 15)
        self.pet.feed(food_amount)
        self.update_status_label()

    def play_pet(self, instance):
        play_time = random.randint(5, 15)
        self.pet.play(play_time)
        self.update_status_label()

    def rest_pet(self, instance):
        rest_time = random.randint(5, 15)
        self.pet.rest(rest_time)
        self.update_status_label()

    def update_status_label(self):
        status = f"Hunger: {self.pet.hunger}\nHappiness: {self.pet.happiness}\nEnergy: {self.pet.energy}"
        self.status_label.text = status

    def run_kivy_app():
        Window.clearcolor = (1, 1, 1, 1)  # Set the window background color to white
        VirtualPetKivyApp().run()
