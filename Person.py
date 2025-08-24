class Person:
    def __init__ (self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def describe(self):
        return f"{self.name} - {self.phone}"

class Client(Person):
    def __init__(self,name:str,phone:str,wallet:float):
        super().__init__(name,phone)
        self.wallet = wallet
    
    def pay(self,amount :float):
        if amount  <= self.wallet:
            self.wallet =  self.wallet - amount
            return True
            # return {"status": True, "message": "Payment successful", "balance": self.wallet}
        else:
            self.wallet = self.wallet
            return False
            # return {"status": False, "message": "Insufficient funds", "balance": self.wallet}
        


# Omolola = Client("Omolola","1234567890",700.0)
# print(Omolola.pay(600.0))