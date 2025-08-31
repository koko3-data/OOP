from Person import Client, ServiceProvider
from Service import Service


class Booking:
    def __init__(self,client : Client , provider :ServiceProvider, service : Service, timeslot :str):
        self.client = client
        self.provider = provider
        self.service = service
        self.timeslot = timeslot

    def total_price(self):
        return self.provider.rate_price(self.service.price_quote())

    def confirm_boooking(self):
        if self.client.pay(self.total_price()) == True:
            return f"Booked {self.service.name} with {self.provider.name} at {self.timeslot} for {self.total_price()} {self.service.currency}."
        else:
            return(
                f"Payment failed for {self.service.name}  - Required amount: {self.total_price()} {self.service.currency}, but you have {self.client.wallet} {self.service.currency}. \n"
                f"Please top up your wallet with {self.total_price() - self.client.wallet} {self.service.currency} to proceed with the booking."
            )

                     