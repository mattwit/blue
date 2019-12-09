from netmiko import ConnectHandler
import getpass

# prompt for hostname,user,pw
host = input('host:')
user1 = 'matthew.witmer'
p = getpass.getpass()

# create device object
device1 = {
    'host': host,
    'username': user1,
    'password': p,
    'device_type': 'extreme_exos',
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_config_from_file('config_change.txt')

net_connect.disconnect()

print(output)