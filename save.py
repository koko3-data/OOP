from Person import Client, ServiceProvider
# from menu import all_clients
import os
import csv

from Service import HaircutService, ManicureService, MassageService, TherapyService
from Booking import Booking

def save_clients_csv(client,filename = 'clients.csv'):
    file_exists  = os.path.exists(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Name', 'Phone', 'Wallet'])  # Header row
            writer.writerow(client.to_csv())
        else:
            writer.writerow(client.to_csv())

def load_clients_csv(filename = 'clients.csv'):
    clients = []
    try:
        with open(filename, mode='r',newline= '') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                client = Client.from_csv(row)
                clients.append(client)
    except FileNotFoundError:
        print(f"No existing file named {filename} found. Starting with an empty client list.")
    return clients

def save_providers_csv(provider,filename = 'providers.csv'):
    file_exists  = os.path.exists(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Name', 'Phone', 'Speciality','Rate_Multiplier'])  # Header row
            writer.writerow(provider.to_csv())
        else:
            writer.writerow(provider.to_csv())

def load_providers_csv(provider,filename = 'providers.csv'):
    providers = []
    try:
        with open(filename, mode='r',newline= '') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                provider = ServiceProvider.from_csv(row)
                providers.append(provider)
    except FileNotFoundError:
        print(f"No existing file named {filename} found. Starting with an empty client list.")
    return providers

def save_services_csv(service,filename = 'services.csv'):
    file_exists  = os.path.exists(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Name', 'Duration (Mins)', 'Base_Price'])  # Header row
            writer.writerow(service.to_csv())
        else:
            writer.writerow(service.to_csv())

def load_services_csv(service,filename = 'services.csv'):
    services = []
    try:
        with open(filename, mode='r',newline= '') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == "Haircut Service":
                   service = HaircutService.from_csv(row)
                   services.append(service)
                elif row[0] == "Manicure Service":
                   service = ManicureService.from_csv(row)
                   services.append(service)
                elif row[0] == "Massage Service":
                   service = MassageService.from_csv(row)
                   services.append(service)
                elif row[0] == "Therapy Service":
                   service = TherapyService.from_csv(row)
                   services.append(service)
        
    except FileNotFoundError:
        print(f"No existing file named {filename} found. Starting with an empty client list.")
    return services

def save_bookings_csv(booking,filename = 'bookings.csv'):
    file_exists  = os.path.exists(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Client', 'Provider', 'Service','Timeslot','Source'])  # Header row
            writer.writerow(booking.to_csv())
        else:
            writer.writerow(booking.to_csv())

def load_bookings_csv(booking,filename = 'bookings.csv'):
    bookings = []
    try:
        with open(filename, mode='r',newline= '') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                booking = Booking.from_csv(row)
                bookings.append(booking)
    except FileNotFoundError:
        print(f"No existing file named {filename} found. Starting with an empty client list.")
    return bookings