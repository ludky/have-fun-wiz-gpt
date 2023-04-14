# main.py

import virtual_pet_tkinter
#import virtual_pet_kivy
import virtual_pet_pyqt

def main():
    print("Choose a GUI framework:")
    print("1. Tkinter")
    print("2. Kivy")
    print("3. PyQt")
    choice = input("Enter the number of the GUI framework: ")

    if choice == "1":
        virtual_pet_tkinter.run_tkinter_app()
    #elif choice == "2":
        #virtual_pet_kivy.run_kivy_app()
    elif choice == "3":
        virtual_pet_pyqt.run_pyqt_app()
    else:
        print("Invalid input. Please choose a valid option.")


'''
from virtual_pet_tkinter import run_tkinter_app
from virtual_pet_kivy import run_kivy_app

def main():
    print("Choose a GUI framework:")
    print("1. Tkinter")
    print("2. Kivy")
    choice = input("Enter the number of the GUI framework: ")

    if choice == "1":
        run_tkinter_app()
    elif choice == "2":
        run_kivy_app()
    else:
        print("Invalid input. Please choose a valid option.")
'''

if __name__ == "__main__":
    main()