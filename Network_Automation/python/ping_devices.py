import re   
from netmiko import ConnectHandler

# Get list of devices from inventory.ini and put the information into a loop?
with open(r'inventory.ini') as file:
    content = file.read()
    ips = ips = re.findall(r'ansible_host=(\d{1,3}(?:\.\d{1,3}){3})', content)
    print(ips)


for ip in ips:

    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": "YOUR_PASSWORD"
    }

    connection = ConnectHandler(**device)

    output = connection.send_command(f"ping {ip}")

    print(f"\n--- {ip} ---")
    print(output)

    connection.disconnect()