# virtual_pet_pyqt.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget
from virtual_pet import VirtualPet
import sys
import random
from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtCore import QTimer, Qt

class VirtualPetPyQtApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pet = VirtualPet("Pet")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Virtual Pet")
        self.setGeometry(100, 100, 300, 250)

        widget = QWidget()
        layout = QVBoxLayout()

        self.status_label = QLabel()
        self.update_status_label()

        feed_button = QPushButton("Feed")
        feed_button.clicked.connect(self.feed_pet)

        play_button = QPushButton("Play")
        play_button.clicked.connect(self.play_pet)

        rest_button = QPushButton("Rest")
        rest_button.clicked.connect(self.rest_pet)

        self.load_dog_animation_frames()

        self.dog_animation_label = QLabel()
        self.dog_animation_label.setAlignment(Qt.AlignCenter)
        self.dog_animation_label.setPixmap(self.dog_animation_frames[0].scaled(self.width(), self.height(), Qt.KeepAspectRatio))


        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.update_dog_animation)
        self.animation_timer.start(100)  # Change this value to control the animation speed

        layout.addWidget(self.status_label)
        layout.addWidget(feed_button)
        layout.addWidget(play_button)
        layout.addWidget(rest_button)
        layout.addWidget(self.dog_animation_label)

        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def load_dog_animation_frames(self):
        self.dog_animation_frames = []
        frame_number = 1

        while True:
            image_path = f"rooney_{frame_number}.jpg"
            if not QImageReader(image_path).canRead():
                break

            self.dog_animation_frames.append(QPixmap(image_path))
            frame_number += 1

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
        self.status_label.setText(status)
    
    def update_dog_animation(self):
        current_frame = self.dog_animation_label.property("frame")
        if current_frame is None or current_frame >= len(self.dog_animation_frames) - 1:
            current_frame = 0
        else:
            current_frame += 1

        self.dog_animation_label.setPixmap(self.dog_animation_frames[current_frame])
        self.dog_animation_label.setProperty("frame", current_frame)

def run_pyqt_app():
    app = QApplication(sys.argv)
    window = VirtualPetPyQtApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_pyqt_app()
