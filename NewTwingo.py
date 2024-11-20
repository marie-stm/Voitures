from Twingo import Twingo

class NewTwingo(Twingo):
    def __init__(self, licenceNumber: str):
        super().__init__(licenceNumber, nbDoors=5)