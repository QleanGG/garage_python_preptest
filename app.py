"""
* create menu
* Crud to cars
* Taking from json file and saving in json file
* helper functions to help with menu and cars

features:
get
add
edit
delete
"""
from helper import menu_selection
from json_helper import read_json

def menu(cars):
    while True:
        print("My Garage")
        print("1 - Get all cars")
        print("2 - add car")
        print("3 - delete car")
        print("4 - edit car")
        print("5 - save cars")
        choice = input("")
        menu_selection(cars,choice)

def main():
    cars = read_json();
    menu(cars)


if __name__ == "__main__":
    main()