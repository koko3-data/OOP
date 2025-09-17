class Person:
    def __init__ (self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def describe(self):
        return f"{self.name}  ({self.phone})"



class Client(Person):
    all_clients : list = []

    def __init__(self,name:str,phone:str,wallet:float):
        super().__init__(name,phone)
        self.wallet = wallet
        
        Client.all_clients.append(self)
    
    @classmethod
    def list_all(cls):
        return [client.describe() for client in cls.all_clients]
    
  
    
    def describe(self):
        return super().describe() + f" - Wallet Balance: {self.wallet}"

        

class ServiceProvider(Person):
    platform_fee = 2
    def __init__ (self, name :str , phone : str, speciality :str , rate_multiplier : float = 1.0):
        super().__init__(name,phone)
        self.speciality = speciality
        self.rate_multiplier = rate_multiplier

    def rate_price(self,base_price:float):
        #you are not using self.amount here because you don't need amount stored  in the object . You just need to use it to calculate the rate price
        #The value for amount is temporary and only used within the method
        return (base_price * self.rate_multiplier)+ self.platform_fee

    def describe(self):
        return super().describe() + f" - {self.speciality}"


# Omolola = Client("Omolola","1234567890",700.0)
# print(Omolola.pay(600.0))

# Tola = ServiceProvider("Tola","+4887654321","Therapist",1.7)
# print(Tola.rate_price(200.0))
# print(Tola.describe())
