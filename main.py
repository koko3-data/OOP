from Person import Client, ServiceProvider
from Service import ManicureService, Service
from Booking import Booking


client1 = Client("Alice", "123-456-7890", 300.0)
provider1 = ServiceProvider("Lola", 881278182, "Manicure", 1.5)
manicure_service = ManicureService("Hybrid_manicure", 120, 100.0 , gel=True)
booking1 = Booking(client1, provider1, manicure_service, "2024-10-01 14:00")
print(booking1.confirm_boooking())

client2 = Client("Bob", "123-456-7890", 50.0)
provider1 = ServiceProvider("Lola", 881278182, "Manicure", 1.5)
manicure_service = ManicureService("Hybrid_manicure", 120, 100.0 , gel=True)
booking2 = Booking(client1, provider1, manicure_service, "2024-10-01 14:00")
print(booking2.confirm_boooking())