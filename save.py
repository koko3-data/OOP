from Person import Client
# from menu import all_clients
import os
import csv

def save_clients_csv(clients,filename = 'clients.csv'):
    file_exists  = os.path.exists(filename)


    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Name', 'Phone', 'Wallet'])  # Header row
            for client in clients:
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

