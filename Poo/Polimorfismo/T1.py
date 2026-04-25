from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now ON")

    def turn_off(self):
        print("Washing machine is now OFF")

machine = WashingMachine()
machine.turn_on()
machine.turn_off()

