class Person:
    def __init__ (self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def describe(self):
        return f"{self.name}  ({self.phone})"


all_clients : list = []
class Client(Person):
    def __init__(self,name:str,phone:str,wallet:float):
        super().__init__(name,phone)
        self.wallet = wallet
        
        all_clients.append(self)

    def list_all(cls):
        return [client.describe() for client in all_clients]
    
    def pay(self,amount :float):
        if amount  <= self.wallet:
            self.wallet =  self.wallet - amount
            return True
            # return {"status": True, "message": "Payment successful", "balance": self.wallet}
        else:
            self.wallet = self.wallet
            return False
            # return {"status": False, "message": "Insufficient funds", "balance": self.wallet}

        
platform_fee = 2
class ServiceProvider(Person):
    def __init__ (self, name :str , phone : str, speciality :str , rate_multiplier : float = 1.0):
        super().__init__(name,phone)
        self.speciality = speciality
        self.rate_multiplier = rate_multiplier

    def rate_price(self,base_price:float):
        #you are not using self.amount here because you don't need amount stored  in the object . You just need to use it to calculate the rate price
        #The value for amount is temporary and only used within the method
        return (base_price * self.rate_multiplier)+ platform_fee

    def describe(self):
        return super().describe() + f" - {self.speciality}"


# Omolola = Client("Omolola","1234567890",700.0)
# print(Omolola.pay(600.0))

# Tola = ServiceProvider("Tola","+4887654321","Therapist",1.7)
# print(Tola.rate_price(200.0))
# print(Tola.describe())
