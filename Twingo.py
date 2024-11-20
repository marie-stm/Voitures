from abc import ABC
from Car import Car

class Twingo(ABC,Car):
    def __init__(self, licenceNumber: str, nbDoors: int = 3):
        super().__init__("Renault", licenceNumber, nbDoors)

    def stop