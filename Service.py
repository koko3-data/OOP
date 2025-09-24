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
    

class HaircutService(Service):
    def __init__(self, name: str, duration_min: int, base_price: float, long_hair: bool = False):
        super(). __init__(name, duration_min, base_price)
        self.long_hair = long_hair
    
    def material_cost(self,total_price: float):
        if self.long_hair:
            return total_price +  30.0

class ManicureService(Service):
    def __init__(self, name: str, duration_min: int, base_price: float, gel: bool = False):
        super(). __init__(name, duration_min, base_price)
        self.gel= gel
    
    def material_cost(self, total_price: float):
        if self.gel:
            return total_price + 20.0


class MassageService(Service):
    def __init__(self, name: str, duration_min: int, base_price: float, deep_tissue: bool = False):
        super(). __init__(name, duration_min, base_price)
        self.deep_tissue = deep_tissue

    def material_cost(self, total_price: float):
        if self.deep_tissue:
            return  total_price * 1.2
       
class TherapyService(Service):
    pass
        
  

# Lola_service = Service("Lola", 60, 200.0)
# print(Lola_service.info())

# Lola_haircut = HaircutService("Lola Haircut", 45, 150.0)
# print(Lola_haircut.price_quote())
# print(Lola_haircut.info())

# Lola_Mani = ManicureService("Lola Manicure", 30, 100.0, gel=False)
# print(Lola_Mani.price_quote())
# print(Lola_Mani.info())

# lola_massage = MassageService("Lola Massage", 90, 300.0, deep_tissue=True)
# print(lola_massage.price_quote())
# print(lola_massage.info())

# lola_therapy = TherapyService("Lola Therapy", 60, 250.0)
# print(lola_therapy.price_quote())
# print(lola_therapy.info())