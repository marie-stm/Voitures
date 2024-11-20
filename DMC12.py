from Car import Car

class DMC12(Car):
    def __init__(self, licenceNumber: str):
        super().__init__("Delorean", licenceNumber, nbDoors=3)

        def fly(self)-> None:
            print("f"{self.licenceNumber}}:"je vole")