class DCar:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
    def say_state(self):
        print("I'm going {} kph!".format(self.speed))
    def accelerate(self):
        self.speed += 5
    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5
    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
     if self.time != 0:
            return self.odometer / self.time
     else:
             pass

if __name__ == '__main__':

    BMW = DCar()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                 "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            BMW.accelerate()
        elif action == 'B':
            BMW.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(BMW.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(BMW.average_speed()))
        BMW.step()
        BMW.say_state()