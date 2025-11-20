from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"



if __name__ == "__main__":
    print("=== Car Example ===")
    my_car = Car(18, 4)
    print(f"Wheel size: {my_car.wheel_size}")
    print(f"Number of wheels: {my_car.wheel_number}")
    print(f"Car goes: {my_car.go()}")
  