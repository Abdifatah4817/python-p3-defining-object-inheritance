class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"




if __name__ == "__main__":
    print("=== Vehicle Example ===")
    my_vehicle = Vehicle(20, 4)
    print(f"Wheel size: {my_vehicle.wheel_size}")
    print(f"Number of wheels: {my_vehicle.wheel_number}")
    print(f"Vehicle goes: {my_vehicle.go()}")
    print(f"Filling tank: {my_vehicle.fill_up_tank()}")