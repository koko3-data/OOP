from Person import Client, ServiceProvider
from Service import Service,ManicureService,HaircutService,MassageService,TherapyService
from save import load_clients_csv, save_clients_csv, load_providers_csv, save_providers_csv ,load_services_csv, save_services_csv 
all_clients = []
all_providers = []
all_services = []

def menu():
    
    all_clients = load_clients_csv('clients.csv') 
    all_providers = load_providers_csv('providers.csv') 
    all_services = load_services_csv('services.csv')
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
         name = input("Enter client name: ").lower()
         phone = input("Enter client phone number: ")
         wallet = float(input("Enter client wallet balance: "))

         client = Client(name, phone, wallet)
         all_clients.append(client)
         save_clients_csv(client, 'clients.csv')
         print(f"\033[1;32m' {client} '\033[0m")
         
     
         

        elif choice == '2':
            name = input("Enter service provider name: ").lower()
            phone = input("Enter service provider phone number: ")
            speciality = input("Enter service provider speciality: ")
            rate_multiplier = float(input("Enter service provider rate multiplier: "))

            provider = ServiceProvider(name, phone, speciality, rate_multiplier)
            all_providers.append(provider)
            save_providers_csv(provider,'providers.csv')
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
              save_services_csv(service,'services.csv')
              print(f"\033[1;35m' {service} '\033[0m")
           
           elif service_type == '2':
              gel = input("Does it include gel? (yes/no): ").strip().lower() == 'yes'
              name = "Manicure Service"
              duration_min = int(input("Enter service duration in minutes: "))
              base_price = float(input("Enter service base price: "))
              service = ManicureService(name, duration_min, base_price, gel)
              all_services.append(service)
              save_services_csv(service,'services.csv')
              print(f"\033[1;35m' {service} '\033[0m")
              

           elif service_type == '3':
             deep_tissue = input("Is it a deep tissue massage? (yes/no): ").strip().lower() == 'yes'
             name = "Massage Service"
             duration_min = int(input("Enter service duration in minutes: "))
             base_price = float(input("Enter service base price: "))
             service = MassageService(name, duration_min, base_price, deep_tissue)
             all_services.append(service)
             save_services_csv(service,'services.csv')
             print(f"\033[1;35m' {service} '\033[0m")

           elif service_type == '4':
              name = "Therapy Service"  
              duration_min = int(input("Enter service duration in minutes: "))
              base_price = float(input("Enter service base price: "))
              service = TherapyService(name, duration_min, base_price)
              all_services.append(service)
              save_services_csv(service,'services.csv')
              print(f"\033[1;35m' {service} '\033[0m")

           else:
              print("Invalid service type selected")
              continue
           
        
        elif choice == '4':
           client_name = input("Filter for clients whose name starts with (leave blank for all):").strip().lower()
           filtered_clients = [client for client in all_clients if client.name.startswith(client_name)]if client_name else all_clients
           if not filtered_clients:
              print("No clients found with that name.")
           else: 
              for index, client in enumerate(filtered_clients, start=1):
                print(f"\033[1;32m'{index}. {client}'\033[0m")
              
              client_for_booking_index = int(input("Select client by number: ")) - 1
              if 0 <= client_for_booking_index < len(filtered_clients):
                 client_for_booking = filtered_clients[client_for_booking_index]

              else:
                 print("Invalid selection.")
                 continue
           
            
        elif choice == '8':
          all_clients = load_clients_csv('clients.csv')
          for client in all_clients:
            print(f"\033[1;35m{client}\033[0m")

             
        elif choice == '9':
          all_providers= load_providers_csv('providers.csv')
          for provider in all_providers:
            print(f"\033[1;35m{provider}\033[0m")

        elif choice == '10':
          all_services= load_services_csv('services.csv')
          for service in all_services:
            print(f"\033[1;35m{service}\033[0m")
         
         

        elif choice == '11':
            print("Thank you for using SaloonBooker. Goodbye!")
            break
          
              
              
   
             

            
        
              
    
            
        
           
           
            
            
        

      
         

        