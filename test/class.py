class Car:
    unit_of_measurement = "km/l"
    def __init__(self, make, model, year,fuel_consumption: float,distance: float,car_age:int):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_consumption = fuel_consumption  
        self.distance = distance
        self.car_age = car_age

    def __str__(self):
        return f"The car was manufactured in {self.year} by {self.make} with {self.model}"

    def car_mileage(self):
        return {self.distance} / {self.fuel_consumption} 

    def estimated_life_usage(self):
        return {self.car_age} * self.car_mileage()