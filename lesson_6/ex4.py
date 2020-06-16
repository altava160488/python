class Car:

    def __init__(self, speed, color, name, is_polis = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = is_polis
        print(f"The car with model \'{self.name}\' and color \'{self.color}\' has initialized!")
        self.go()
        self.show_speed()

    def go(self):
        print("Go!")

    def stop(self):
        print("Stop!")

    def turn(self, direction):
        print(f"Turn {direction}!")

    def show_speed(self):
        print(f"Current speed is equal to {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_polis = False):
        super(TownCar, self).__init__(speed, color, name, is_polis)

    def show_speed(self):
        print("Your speed is raiser then 60") if self.speed > 60 else print(f"Current speed is equal to {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_polis = False):
        super(SportCar, self).__init__(speed, color, name, is_polis)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_polis = False):
        super(WorkCar, self).__init__(speed, color, name, is_polis)

    def show_speed(self):
        print("Your speed is raiser then 40") if self.speed > 40 else print(f"Current speed is equal to {Car.speed}")


class PolisCar(Car):
    def __init__(self, speed, color, name, is_polis = True):
        super(PolisCar, self).__init__(speed, color, name, is_polis)


t_car = TownCar(80, "blue", "Town")
t_car.turn("left")
t_car.stop()
print(t_car.is_polis)
print()
p_car = PolisCar(80, "black", "Polis")
p_car.color = 'white'
p_car.turn("right")
print(p_car.color)
print(p_car.is_polis)
