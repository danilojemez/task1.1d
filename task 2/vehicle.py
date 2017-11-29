import sys

class Vehicle(object):
    vehicle_id = 0
    vehicles_sold = []

    def __init__(self,year,mileage,purchase_price,serial_number):
        try:
            if isinstance(year,int) == False:
                raise ValueError
            if isinstance(mileage, int) == False:
                raise ValueError
            if isinstance(purchase_price,int) == False:
                raise ValueError
        except ValueError:
            print("The values enterrred are not of type integer")
        else:
            self.year = year
            self.mileage = mileage
            self.purchase_price = purchase_price
            self.serial_number = serial_number
            self.vehicle_id = Vehicle.generate_vehicle_id(self)
            Vehicle.vehicle_id += 1

    def __str__(self):
        return str(self.vehicle_id)

    def get_id(self):
        return self.vehicle_id

    @staticmethod
    def generate_vehicle_id(self):
        return 100000+Vehicle.vehicle_id
    ######## CODE MISSING HERE

class Car(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,doors):
        try:
            if isinstance(year,int) == False:
                raise ValueError
            if isinstance(mileage, int) == False:
                raise ValueError
            if isinstance(purchase_price,int) == False:
                raise ValueError
        except ValueError:
            print("The Class arguments year, mileage and purchase_price have to be of type int")
        else:
            self.year = year
            self.mileage = mileage
            self.purchase_price = purchase_price
            self.serial_number = serial_number
            self.doors = doors
            self.__wheels = 4
            self.vehicle_id = Vehicle.generate_vehicle_id(self)
            Vehicle.vehicle_id += 1

class Lorry(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,wheels,doors=2):
        try:
            if isinstance(year,int) == False:
                raise ValueError
            if isinstance(mileage, int) == False:
                raise ValueError
            if isinstance(purchase_price,int) == False:
                raise ValueError
        except ValueError:
            print("The Class arguments year, mileage and purchase_price have to be of type int")
        else:
            self.year = year
            self.mileage = mileage
            self.purchase_price = purchase_price
            self.serial_number = serial_number
            self.wheels = wheels
            self.doors = doors
            self.vehicle_id = Vehicle.generate_vehicle_id(self)
            Vehicle.vehicle_id += 1
        
class Motorcycle(Vehicle):

    classic_count = 0

    def __init__(self,year,mileage,purchase_price,serial_number,classic=False):
        try:
            if isinstance(year,int) == False:
                raise ValueError
            if isinstance(mileage, int) == False:
                raise ValueError
            if isinstance(purchase_price,int) == False:
                raise ValueError
        except ValueError:
            print("The Class arguments year, mileage and purchase_price have to be of type int")
        else:
            self.year = year
            self.mileage = mileage
            self.purchase_price = purchase_price
            self.serial_number = serial_number
            self.__classic = classic
            self.vehicle_id = Vehicle.generate_vehicle_id(self)
            Vehicle.vehicle_id += 1
            if self.__classic is True:
                Motorcycle.classic_count += 1

### test cases ###

# initialising vehicle instances

Veh1 = Vehicle(2008,65000,7500,"34567851g4")
Veh2 = Car(2007,125000,5500,"e44653ftu1",4)
Veh3 = Car(2012,45000,8900,"gf5622iguz",doors=2)
Veh4 = Lorry(2005,180000,16000,"hbh997123f",6)
Veh5 = Lorry(2013,30000,35000,"hjbf17jbkh",8,4)
Veh6 = Motorcycle(1975,75500,40000,"bh545664rh",True)

print(Veh1,Veh2,Veh3,Veh4,Veh5,Veh6)
#prints 	100000 	100001 	100002 	100003 	100004 	100005

Veh7 = Motorcycle("year",10000,25000,"bjhgss4rdh",False)
# instance Veh7 generates an exception (ValueError) (uncomment to test)