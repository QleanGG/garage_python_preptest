def get_cars(cars):
    for car in cars:
        print(car)

def add_car(cars):
    new_model = input("Enter model: ")
    new_brand = input("Enter brand: ")
    new_color = input("Enter color: ")

    new_car = {"model":new_model, "brand":new_brand, "color":new_color}
    cars.append(new_car)
    return print("new car Added: ", new_car)

def delete_car(cars):
    car_select = int(input("choose car number: "))
    cars.pop(car_select)
    return print("car deleted")

