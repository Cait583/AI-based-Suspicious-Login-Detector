import pandas as pd  # This handles data in tables like Excel to simulate the login records
import datetime  # This imports Python's built-in module that works with time and dates to check when a login occurred
import random  # This will simulate login data like fake login times, IP addresses, and countries
import ipaddress  # This lets Python work with IP addresses like verifying if they are valid or seeing if there is a suspicious range

def generate_fake_logins(num_entries=10):  # This will generate 10 fake logins by default
    logins = []  # This is creating an empty list called logins; it will store each fake login created
    countries = ['US', 'CN', 'RU', 'BR', 'IN', 'DE', 'FR', 'NG', 'KR', 'IR']  # This creates a list of country codes

    for _ in range(num_entries):  # This for loop will run num_entries times; each loop creates one fake login
        login_time = datetime.datetime.now() - datetime.timedelta(minutes=random.randint(1, 10000))  # Generates a fake timestamp
        ip = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))  # Generates a random but valid IP address
        country = random.choice(countries)  # Randomly picks a country code for the login origin

        logins.append({  # This adds the generated login as a dictionary to the list
            'timestamp': login_time,
            'ip': ip,
            'country': country
        })

    return logins  # Returns the list of fake logins
