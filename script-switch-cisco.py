from netmiko import ConnectHandler


device = {
    "device_type": "cisco_ios_telnet",
    "ip": "172.16.0.1",
    "username": "admin",
    "password": "",
    "secret": "",
    "port": 23,
}


commands = [
    "enable",
    "show ip int bri",
    "show running-config | include access-list",
    "show running-config | include ip nat",
    "show interfaces status",
    "show vlan brief",
    "show cdp neighbors",
    "show lldp neighbors",

]

output_file = "output.txt"


with ConnectHandler(**device) as net_connect:

    net_connect.write_channel("enable\n")

    net_connect.write_channel("sid123145\n")


    with open(output_file, "w") as file:
        for command in commands:
            file.write(f"Команда: {command}\n")
            output = net_connect.send_command(command)
            file.write(output)
            file.write("="*50 + "\n")
