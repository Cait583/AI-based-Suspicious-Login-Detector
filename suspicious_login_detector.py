import pandas as pd  # Handles data in tables like Excel to simulate the login records
import datetime  # Works with time and dates to check when a login occurred
import random  # Simulates login data like fake login times, IP addresses, and countries
import ipaddress  # Works with IP addresses for validation and checks

def generate_fake_logins(num_entries=10):  # Generates 10 fake logins by default
    logins = []  # Empty list to store each fake login
    countries = ['US', 'CN', 'RU', 'BR', 'IN', 'DE', 'FR', 'NG', 'KR', 'IR']  # Country codes to pick from
    for _ in range(num_entries):  # Loop to generate each login
        login_time = datetime.datetime.now() - datetime.timedelta(minutes=random.randint(1, 10000))  # Fake timestamp
        ip = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))  # Fake IP address
        country = random.choice(countries)  # Random country from list
        logins.append({  # Add login record to list
            'timestamp': login_time,
            'ip': ip,
            'country': country
        })
    return logins  # Return the list of fake logins

# Generate 10 fake login records using our function
logins = generate_fake_logins(10)

# Convert the list of login dictionaries into a pandas DataFrame (table)
df = pd.DataFrame(logins)

# Print the DataFrame to show the fake login data in a neat tabular format
print(df)
