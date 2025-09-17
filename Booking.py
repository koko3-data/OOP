from Person import Client, ServiceProvider
from Service import Service


class Booking:
    source_default = "SalonBooker"
    def __init__(self, client: Client, provider: ServiceProvider, service: Service, timeslot: str, source: str = None):
        self.client = client
        self.provider = provider
        self.service = service
        self.timeslot = timeslot
        self.source = source if source else self.source_default

    def total_price(self):
        return self.provider.rate_price(self.service.price_quote())
    
    def pay(self,total_amount: float):
        total_amount = self.total_price()
        if total_amount <= self.client.wallet :
            self.client.wallet -= total_amount
            print(f"Payment successful. New wallet balance: {self.client.wallet} {self.service.currency}")
            return True      
        else:
            print(f"Payment failed. Insufficient funds in wallet: {self.client.wallet} {self.service.currency}") 
            return False   


    def confirm_booking(self):
       user_input = input(f"Will you like to pay for service now ? (yes/no): ").strip().lower()
       if user_input == 'yes':
          
           if self.pay(self.total_price()) == True:
               self.confirm_booking = True
               return f"Booking confirmed: {self.service.name} with {self.provider.name} at {self.timeslot} for {self.total_price()} {self.service.currency} via {self.source}."
           else:
                self.confirm_booking = False
                return "Booking failed due to insufficient funds."
       else:
            self.confirm_booking = True
            return f"Booked {self.service.name} with {self.provider.name} at {self.timeslot} for {self.total_price()} {self.service.currency} via {self.source} without payment."
    
    

    # def process_booking(bookings : list):
    #     messages = []
    #     for object in bookings:
    #         if hasattr(object, 'confirm_boooking') and callable(object.confirm_boooking):
    #             messages.append(object.confirm_boooking())
    #     return messages
    

    def cancel_booking(self,confirm_booking: bool = True):
        if self.confirm_booking == True :
            user_input = input(f'Are you sure you want to cancel booking? (yes/no):').strip().lower()
            if user_input == 'yes' :
                refund_amount = 0.9 * self.total_price()
                self.client.wallet += refund_amount
                return f"Booking cancelled. Refund of {refund_amount} {self.service.currency} processed. New wallet balance: {self.client.wallet} {self.service.currency}."
            else:
                return "Cancellation aborted. Booking remains active."
        else:
            return "No active booking to cancel."