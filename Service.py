class Service:

    currency = "PLN" #This is a class field/attribute shared by all objects , differnt from instance fields/attributes
    
    def __init__ (self, name: str ,duration_min : int, base_price : float): #instance fields although shared by objects inheriting it , they are for declaring data unique to each object
        self.name  = name
        self.duration_min = duration_min
        self.base_price = base_price

    def price_quote(self):
        return self.base_price
    
    def info(self):
        return f"{self.name} - {self.duration_min}min -{self.price_quote()} {self.currency}" 



# Lola_service = Service("Lola", 60, 200.0)
# print(Lola_service.info())