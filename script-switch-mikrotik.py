from netmiko import ConnectHandler

device = {
    "device_type": "mikrotik_routeros",
    "ip": "172.16.0.1",
    "port": 22,
    "username": "admin",
    "password": "",
}

commands = [
    "/system resource print",
    "/interface print",
    "/ip dhcp-client print"
]

output_file = "output_routeros.txt"

with ConnectHandler(**device) as net_connect:
    with open(output_file, "w") as file:
        for command in commands:
            file.write(f"Команда: {command}\n")
            output = net_connect.send_command(command)
            file.write(output)
            file.write("="*50 + "\n")