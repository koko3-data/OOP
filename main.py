from Person import Client, ServiceProvider
from Service import ManicureService, Service
from Booking import Booking



client1 = Client("Alice", "123-456-7890", 400.0)
# print(client1.pay(100))
# print(client1.describe())
provider1 = ServiceProvider("Lola", 881278182, "Manicure", 1.5)
manicure_service = ManicureService("Hybrid_manicure", 120, 100.0 , gel=True)
manicure_service2 = ManicureService("Hybrid_manicure", 240, 220.0 , gel=True)
# print(provider1.rate_price(manicure_service.price_quote()))
booking1 = Booking(client1, provider1, manicure_service, "2024-10-01 14:00")
booking2 = Booking(client1, provider1, manicure_service2, "2024-10-01 14:00")
# # print(booking1.total_price())
booking_confirmation1 = (booking1.confirm_booking())
booking_confirmation2 = (booking2.confirm_booking())
# print(booking1.cancel_booking())

# client2 = Client("Bob", "123-456-7890", 50.0)
# provider2 = ServiceProvider("Lola", 881278182, "Manicure", 1.5)
# manicure_service2 = ManicureService("Hybrid_manicure", 120, 100.0 , gel=True)
# booking2 = Booking(client2, provider1, manicure_service, "2024-10-01 14:00")
# booking_confirmation2 = booking2.confirm_booking()

# client3 = Client("Charlie", "987-654-3210", 200.0)
# provider3 = ServiceProvider("Dave", 881278183, "Massage", 1.2)
# massage_service = Service("Full Body Massage", 60, 150.0)
# booking3 = Booking(client3, provider3, massage_service, "2024-10-02 16:00")
# booking_confirmation3 = booking3.confirm_booking()
# # print(booking3.cancel_booking())


# # print(Client.list_all())

# print(Booking.process_booking())
# # print(([booking1],[booking2],[booking3]).process_booking())

# # cl4 = Client()

# # # messages = [booking_confirmation1, booking_confirmation2, booking_confirmation3]
# # # all_bookings = process_booking(messages)
# # # print(all_bookings)


