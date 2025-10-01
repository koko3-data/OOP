from Person import Client, ServiceProvider


def menu():
    while True:
        print("Welcome to SaloonBooker!")
        print("1. Add client : ")
        print("2. Register Service Provider: ")
        print("3. Make Booking: ")
        print("4. Confirm Booking: ")
        print("5. Cancel Booking: ")
        print("6.View Payment status: ")
        print("7. List all clients: ")
        print("8. List all Service Providers: ")
        print("9. List all Services")
        print("10. Quit: ")
        
        choice = input("Enter your choice (1 - 10) : ")
        if choice == '1':
         name = input("Enter client name: ")
         phone = input("Enter client phone number: ")
         wallet = float(input("Enter client wallet balance: "))

         client = Client(name, phone, wallet)
         print(f"Client: {client.describe()} added successfully.")
         return client.describe()

        elif choice == '2':
            name = input("Enter service provider name: ")
            phone = input("Enter service provider phone number: ")
            speciality = input("Enter service provider speciality: ")
            rate_multiplier = float(input("Enter service provider rate multiplier: "))

            provider = ServiceProvider(name, phone, speciality, rate_multiplier)
            print(f"Service Provider: {provider.describe()} registered successfully.")
            return provider.describe()
        
        # elif choice == '3':
           
            
            
        

      
         

        