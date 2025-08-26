from Person import Client, ServiceProvider
import Service


class Booking:
    def __init__(self,client : Client , provider :ServiceProvider, service : Service, timeslot :str):
        self.client = client
        self.provider = provider
        self.service = service
        self.timeslot = timeslot

    def total_price(self):
        return self.provider.rate_price(self.service.price_quote())
    
