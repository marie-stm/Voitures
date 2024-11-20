from DMC12 import DMC12
from OldTwingo import OldTwingo

    docCar = DMC12( "OutATime")
    docCar.start()
    print(docCar.nbDoors)
    print(docCar.brand)

    myFirstTwingo = OldTwingo("1234 WW 33")
    myFirstTwingo.start()

    docCar.fly()
