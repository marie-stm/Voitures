from abc import ABC
from random import randint

class Car(ABC):
    __brand: str
    __licenceNumber: str
    __nbDoors: int

    def __init__(self, brand: str, licenceNumber: str, nbDoors: int):
        self.brand = brand
        self.licenceNumber = licenceNumber
        self.nbDoors = nbDoors

    @property
    def brand(self)->str:
        return self.__brand

    @brand.setter
    def brand(self, brand)->None:
        self.__brand = brand

    @property
    def licenceNumber(self)->str:
        return self.__licenceNumber

    @licenceNumber.setter
    def licenceNumber(self, licenceNumber)->None:
        self.__licenceNumber = licenceNumber

    @property
    def nbDoors(self)-> int:
        return self.__nbDoors

    @nbDoors.setter
    def nbDoors(self, nbDoors)->None:
      self.__nbDoors = nbDoors

    def start(self):
        print(f"{self.licenceNumber}: I START")

    def stop(self):
        print(f"{self.licenceNumber}:I STOP")