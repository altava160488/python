import time

class TrafficLight:
    __color = {1: ['red', 7], 2: ['yellow', 2], 3: ['green', 5], 4: ['yellow', 2]}

    def running(self):
        for k, v in TrafficLight.__color.items():
            print(v[0])
            time.sleep(v[1])

a = TrafficLight()
while True:
    a.running()
