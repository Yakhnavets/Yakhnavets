from datetime import datetime
class Vehicle():

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int):
        self.__maxVelocity = maxVelocity
        self.__engine = engine
        self.__engineType = engineType
        self.__power = power
        self.__mass = mass
        self.__paylod = paylod
        self.__make = make
        self.__model = model
        self.__year = year
        self.__warrantyPeriod = warrantyPeriod
        self.__autopilot = autopilot
        self.__vin = vin
        self.__maxRange = maxRange
        

    def get_maxVelocity(self):
        return self.__maxVelocity

    def set_maxVelocity(self, maxVelocity):
        self.__maxVelocity = maxVelocity

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    def get_engineType(self):
        return self.__engineType

    def set_engineType(self, engineType):
        self.__engineType = engineType

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    def get_mass(self):
        return self.__mass

    def set_mass(self, mass):
        self.__mass = mass

    def get_paylod(self):
        return self.__paylod

    def set_paylod(self, paylod):
        self.__paylod = paylod

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model


    def set_year(self):
        return self.__year

    def get_year(self, year):
        self.__year = year

    def get_warrantyPeriod(self):
        return self.__warrantyPeriod

    def set_warrantyPeriod(self, warrantyPeriod):
        self.__warrantyPeriod = warrantyPeriod

    def get_autopilot(self):
        return self.__autopilot

    def set_autopilot(self, autopilot):
        self.__autopilot = autopilot

    def get_vin(self):
        return self.__vin

    def set_vin(self, vin):
        self.__vin = vin

    def get_maxRange(self):
        return self.__maxRange

    def set_maxRange(self, maxRange):
        self.__maxRange = maxRange

    maxVelocity = property(get_maxVelocity, set_maxVelocity)
    engine = property(get_engine, set_engine)
    engineType = property(get_engineType, set_engineType)
    power = property(get_power, set_power)
    mass = property(get_mass, set_mass)
    paylod = property(get_paylod, set_paylod)
    make = property(get_make, set_make)
    model = property(get_model, set_model)  
    year = property(get_year, set_year)
    warrantyPeriod = property(get_warrantyPeriod, set_warrantyPeriod)
    outopilot = property(get_autopilot, set_autopilot)
    vin = property(get_vin, set_vin)
    maxRange = property(get_maxRange, set_maxRange)

    def start_engine(self):
        print("youve just started the engine\n")
    
    def test_system(self):
        print("system is fine\n")

    def move(self, range):
        print(f'youve driven {range}\n')

    def stop(self):
        print("stoppp\n")

    def load_cargo(self,amount):
        print(f"youve loaded {amount} kg")


class Wheeled(Vehicle):

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, axisCount:int,wheelsCount:int):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__axisCount = axisCount
        self.__wheelsCount = wheelsCount

    def get_axisCount(self):
        return self.__axisCount

    def set_axisCount(self, axisCount):
        self.__axisCount = axisCount

    def get_wheelsCount(self):
        return self.__wheelsCount

    def set_wheelsCount(self, wheelsCount):
        self.__wheelsCount = wheelsCount
        
    axisCount = property(get_axisCount, set_axisCount)
    wheelsCount = property(get_wheelsCount, set_wheelsCount)
    
    #def move(self, range):

class Car(Wheeled):

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, axisCount:int, wheelsCount:int, doorCount:int, bodyType:str, color:str,options:list,automatedGears:bool ):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange, wheelsCount, axisCount)
        self.__doorCount = doorCount
        self.__bodyType = bodyType
        self.__color = color
        self.__options = options
        self.__automatedGears = automatedGears

    def get_doorCount(self):
        return self.__doorCount

    def set_doorCount(self, doorCount):
        self.__doorCount = doorCount

    def get_bodyType(self):
        return self.__bodyType

    def set_bodyType(self, bodyType):
        self.__bodyType = bodyType

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_options(self):
        return self.__options

    def set_options(self, options):
        self.__options = options

    def get_automatedGears(self):
        return self.__automatedGears

    def set_automatedGears(self, automatedGears):
        self.__automatedGears = automatedGears

    def start_engine(self):
        return super().start_engine(self)

    def test_system(self):
        return super().test_system(self)

    def load_cargo(self, amount):
        return super().load_cargo(self, amount)


    def load_fuel(self, amount):
        print(f"{amount} fuel has been filled in")

    def stop(self):
        return super().stop(self)

    doorCount = property(get_doorCount, set_doorCount)
    bodyType = property(get_bodyType, set_bodyType)
    color = property(get_color, set_color)
    options = property(get_options, set_options)
    automatedGears = property(get_automatedGears, set_automatedGears)


class Air(Vehicle):
    
    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, wingsCount:int, engineCount:int, maxAltitude:int ):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__wingsCount = wingsCount
        self.__engineCount = engineCount
        self.__maxAltitude = maxAltitude

    def get_wingsCount(self):
        return self.__wingsCount

    def set_wingsCount(self, wingsCount):
        self.__wingsCount = wingsCount

    def get_engineCount(self):
        return self.__engineCount

    def set_engineCount(self, engineCount):
        self.__engineCount = engineCount

    def get_maxAltitude(self):
        return self.__maxAltitude

    def set_maxAltitude(self, maxAltitude):
        self.__maxAltitude = maxAltitude

    def move(self, range):
        print(f"there is enought fuel for {range} km")

    def stop(self):
        print("the plane has been landed")

    engineCount = property(get_engineCount, set_engineCount)
    wingsCount = property(get_wingsCount, set_wingsCount)
    maxAltitude = property(get_maxAltitude, set_maxAltitude)
    




class AirPlane(Air, Wheeled):
    
    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, wingsCount:int, engineCount:int, maxAltitude:int, passangersCount:int, classType:str, minRunway:int, runwayType:str, entranceCount:int ):
        Air.__init__(make, model, engine, engineType, maxVelocity, mass, year, warrantyPeriod, vin, wingsCount, engineCount, maxAltitude, autopilot, maxRange)
        Wheeled.__init__(self, engine, engineType, maxVelocity)
        self.__passangersCount = passangersCount
        self.__classType = classType
        self.__minRunway = minRunway
        self.__runwayType = runwayType
        self.__entranceCount = entranceCount

    def get_passangersCount(self):
        return self.__passangersCount

    def set_passangersCount(self, passangersCount):
        self.__passangersCount = passangersCount

    def get_classType(self):
        return self.__classType

    def set_classType(self, classType):
        self.__classType = classType

    def get_minRunway(self):
        return self.__minRunway

    def set_minRunway(self, minRunway):
        self.__minRunway = minRunway

    def get_runwayType(self):
        return self.__runwayType

    def set_runwayType(self, runwayType):
        self.__runwayType = runwayType

    def get_entranceCount(self):
        return self.__entranceCount

    def set_entranceCount(self, entranceCount):
        self.entranceCount = entranceCount

    def load_cargo(self, amount):
        return Vehicle.load_cargo(self, amount)

    def start_engine(self):
        return Vehicle.start_engine(self)

    def takeOff(self):
        print("get outta here")

    def stop(self):
        return Air.stop(self)

    def test_system(self):
        return Vehicle.test_system(self)


    passangersCount = property(get_passangersCount, set_passangersCount)
    classType = property(get_classType, set_classType)
    minRunway = property(get_minRunway, set_minRunway)
    runwayType = property(get_runwayType, set_runwayType)
    entranceCount = property(get_entranceCount, set_entranceCount)

class Water(Vehicle):
    

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, displacement:int, underWaterSupport:bool, engineCount:int):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__displacement = displacement
        self.__underWaterSupport = underWaterSupport
        self.__engineCount = engineCount

    def get_displacement(self):
        return self.__displacement

    def set_displacement(self, displacement):
        self.__displacement = displacement

    def get_underWaterSupport(self):
        return self.__underWaterSupport

    def set_underWaterSupport(self, underWaterSupport):
        self.__underWaterSupport = underWaterSupport

    def get_engineCount(self):
        return self.__engineCount

    def set_engineCount(self, engineCount):
        self.__engineCount = engineCount

    def move(self, range):
        return super().move(self, range)

    def stop(self):
        return super().stop(self)


    displacement = property(get_displacement, set_displacement)
    underWaterSupport = property(get_underWaterSupport, set_underWaterSupport)
    engineCount = property(get_engineCount, set_engineCount)


class Jetski(Water):
    

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, displacement:int, underWaterSupport:bool, engineCount:int, color:str):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def start_engine(self):
        return Vehicle.start_engine(self)

    def move(self, range):
        return Vehicle.move(self, range)

    def test_system(self):
        print(Vehicle.test_system(self))

 

    color = property(get_color, set_color)





class Rail(Vehicle):

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, axisCount:int,railsWidth:int):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__railsWidth = railsWidth
        self.__maxRange = maxRange

    def get_railsWidth(self):
        return self.__railsWidth

    def set_railsWidth(self, railsWidth):
        self.__railsWidth = railsWidth

    def get_maxRange(self):
        return self.__maxRange

    def set_maxRange(self, maxRange):
        self.__maxRange = maxRange

    def move(self, range):
        return Vehicle.move(self, range)

    def stop(self):
        return Vehicle.stop(self)

    railsWidth = property(get_railsWidth, set_railsWidth)
    maxRange = property(get_maxRange, set_maxRange)





class Train(Rail):
    

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, axisCount:int,railsWidth:int, locomotivesCount:int, maxEmptyCarts:int, cartsCount:int):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, railsWidth)
        self.__locomotivesCount = locomotivesCount
        self.__maxEmptyCarts = maxEmptyCarts
        self.__cartsCount = cartsCount

    def get_locomotivesCount(self):
        return self.__locomotivesCount

    def set_locomotivesCount(self, locomotivesCount):
        self.__locomotivesCount = locomotivesCount

    def get_maxEmptyCarts(self):
        return self.__maxEmptyCarts

    def set_maxEmptyCarts(self, maxEmptyCarts):
        self.__maxEmptyCarts = maxEmptyCarts

    def get_cartsCount(self):
        return self.__cartsCount

    def set_cartsCount(self, cartsCount):
        self.__cartsCount = cartsCount

    def move(self, range):
        return Rail.move(self, range)

    def stop(self):
        return Rail.stop(self)

    def start_engine(self):
        return Vehicle.start_engine(self)

    def test_system(self):
        return Vehicle.test_system(self)

    locomotivesCount = property(get_locomotivesCount, set_locomotivesCount)
    _maxEmptyCarts= property(get_maxEmptyCarts, set_maxEmptyCarts)
    cartsCount = property(get_cartsCount, set_cartsCount)


class Helicopter(Air):

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, wingsCount:int, wingCount:int):
        super.__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod, autopilot, vin, maxRange)
        
        self.__wingCount = wingCount

    def get_wingCount(self):
        return self.__wingCount

    def set_wingCount(self, wingCount):
        self.__wingCount = wingCount

    def start_engine(self):
        return Vehicle.start_engine(self)


    def load_fuel(self, amount):
        print(f'{amount} fuel has to be filled in before flight')

    def stop(self):
        return Air.stop(self)

    def test_system(self):
        return Vehicle.test_system(self)


    wingsCount = property(get_wingCount, set_wingCount)



class Bicycle(Wheeled):
    

    def __init__(self, maxVelocity: int, engine:str, engineType:str, power:int, mass:int, model:int, paylod:int, make:str, year:datetime, warrantyPeriod:datetime, autopilot:bool, vin:str, maxRange:int, axisCount:int,wheelsCount:int, speedsCount:int):
        super().__init__(self, maxVelocity, engine, engineType, power, mass, model, paylod, make, year, warrantyPeriod,  vin, maxRange, axisCount, wheelsCount)
        self.__speedsCount = speedsCount

    def get_speedsCount(self):
        return self.__speedsCount

    def set_speedsCount(self, speedsCount):
        self.__speedsCount = speedsCount

    def start_engine(self):
        return Wheeled.start_engine(self)

    speedsCount = property(get_speedsCount, set_speedsCount) 

