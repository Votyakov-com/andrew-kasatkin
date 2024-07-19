class Device:
    def __init__(self, name, turn=False):
        self.name = name
        self.turn = turn
    def turn_on(self):
        print(f'{self.name} is turn on.')
        self.turn = True
    def turn_off(self):
        print(f'{self.name} is turn off.')
        self.turn = False

class SmartHome:
    def __init__(self, args):
        self.devices = args
    def turn_on(self):
        for item in self.devices:
            item.turn_on()
    def turn_off(self):
        for item in self.devices:
            item.turn_off()

class Lamp(Device):
    def __init__(self):
        super().__init__(name='Lamp')
class MotionSensor(Device):
    def __init__(self):
        super().__init__(name='MotionSensor')
class Thermostat(Device):
    def __init__(self):
        super().__init__(name='Thermostat')




lamp = Lamp()
motion_sensor = MotionSensor()
thermostat = Thermostat()

smart_home = SmartHome([lamp, motion_sensor, thermostat])

smart_home.turn_on()
print()
print('Good night!')
print()
smart_home.turn_off()
