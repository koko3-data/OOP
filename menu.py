from Person import Client, ServiceProvider
from Service import Service,ManicureService,HaircutService,MassageService,TherapyService


def menu():
    while True:
        print("Welcome to SaloonBooker!")
        print("1. Add client : ")
        print("2. Register Service Provider: ")
        print("3. Add Service: ")
        print("4. Make Booking: ")
        print("5. Confirm Booking: ")
        print("6. Cancel Booking: ")
        print("7.View Payment status: ")
        print("8. List all clients: ")
        print("9. List all Service Providers: ")
        print("10. List all Services")
        print("11. Quit: ")
        
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
        
        elif choice == '3':
           name = input("Enter service name: ")
           duration_min = int(input("Enter service duration in minutes: "))
           base_price = float(input("Enter service base price: "))
           print("Select service type:")
           print("1. Haircut Service")
           print("2. Manicure Service")
           print("3. Massage Service")
           print("4. Therapy Service")
           service_type = input("Enter your choice (1-4): ")
           if service_type == '1':
              long_hair = input("Is it for long hair? (yes/no): ").strip().lower() == 'yes'
              service = HaircutService(name, duration_min, base_price, long_hair)
           
           elif service_type == '2':
              gel = input("Does it include gel? (yes/no): ").strip().lower() == 'yes'
              service = ManicureService(name, duration_min, base_price, gel)

           elif service_type == '3':
             deep_tissue = input("Is it a deep tissue massage? (yes/no): ").strip().lower() == 'yes'
             service = MassageService(name, duration_min, base_price, deep_tissue)

           elif service_type == '4':
             service = TherapyService(name, duration_min, base_price)
              
        #  
             

            
        
              
    
            
        
           
           
            
            
        

      
         

        