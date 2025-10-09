from Person import Client, ServiceProvider
from Service import Service,ManicureService,HaircutService,MassageService,TherapyService

all_clients = []
all_providers = []
all_services = []

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
        
        choice = input("Enter your choice (1 - 11) : ")
        if choice == '1':
         name = input("Enter client name: ")
         phone = input("Enter client phone number: ")
         wallet = float(input("Enter client wallet balance: "))

         client = Client(name, phone, wallet)
         all_clients.append(client)
         for client in all_clients:
          print(f"\033[1;32m' {client} '\033[0m")
         

        elif choice == '2':
            name = input("Enter service provider name: ")
            phone = input("Enter service provider phone number: ")
            speciality = input("Enter service provider speciality: ")
            rate_multiplier = float(input("Enter service provider rate multiplier: "))

            provider = ServiceProvider(name, phone, speciality, rate_multiplier)
            all_providers.append(provider)
            for provider in all_providers:
             print(f"\033[1;34m' {provider} '\033[0m")
           
            
        
        elif choice == '3':
           print("Select available service type:")
           print("1. Haircut Service")
           print("2. Manicure Service")
           print("3. Massage Service")
           print("4. Therapy Service")
           service_type = input("Enter your choice (1-4): ")
           if service_type == '1':
              long_hair = input("Is it for long hair? (yes/no): ").strip().lower() == 'yes'
              name = "Haircut Service"
              duration_min = int(input("Enter service duration in minutes: "))
              base_price = float(input("Enter service base price: "))
              service = HaircutService(name, duration_min, base_price, long_hair)
              all_services.append(service)
              for service in all_services:
               print(f"\033[1;35m' {service} '\033[0m")
           
           elif service_type == '2':
              gel = input("Does it include gel? (yes/no): ").strip().lower() == 'yes'
              name = "Manicure Service"
              duration_min = int(input("Enter service duration in minutes: "))
              base_price = float(input("Enter service base price: "))
              service = ManicureService(name, duration_min, base_price, gel)
              all_services.append(service)
              for service in all_services:
               print(f"\033[1;35m' {service} '\033[0m")

           elif service_type == '3':
             deep_tissue = input("Is it a deep tissue massage? (yes/no): ").strip().lower() == 'yes'
             name = "Massage Service"
             duration_min = int(input("Enter service duration in minutes: "))
             base_price = float(input("Enter service base price: "))
             service = MassageService(name, duration_min, base_price, deep_tissue)
             all_services.append(service)
             for service in all_services:
               print(f"\033[1;35m' {service} '\033[0m")

           elif service_type == '4':
              name = "Therapy Service"  
              duration_min = int(input("Enter service duration in minutes: "))
              base_price = float(input("Enter service base price: "))
              service = TherapyService(name, duration_min, base_price)
              all_services.append(service)
              for service in all_services:
               print(f"\033[1;35m' {service} '\033[0m")

           else:
              print("Invalid service type selected")
              continue
            
         

        elif choice == '11':
            print("Thank you for using SaloonBooker. Goodbye!")
            break
          
              
              
   
             

            
        
              
    
            
        
           
           
            
            
        

      
         

        