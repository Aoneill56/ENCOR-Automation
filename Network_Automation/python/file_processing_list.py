with open('/home/aaron/Automation/Master Network Automation with Python for Network Engineers - Course Resources/File Processing/devices.txt') as f:
    content = f.read().splitlines()
    for x in content:
        device = x.split(":")
        print("\n")

        print(f"Hostname {device[0]}")
        print(f"IP {device[1]}")
   
    
        print(f"Pinging  {device[0]} on the IP --{device[1]}--")
        