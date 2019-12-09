from netmiko import ConnectHandler
from datetime import datetime
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

start_time = datetime.now()

net_connect = ConnectHandler(**device1)

# define and open text file
file = open(host + '_exos.txt', 'w')

command = input('Enter command:')

output = net_connect.send_command(command)

net_connect.disconnect()

print("\n")
print("#" * 80)
print("\n")
print(output)
print("#" * 80) 
print("\n")

end_time = datetime.now()

print("Script Run Time: {}".format(end_time - start_time))
print("\n")

# Write output to file and close
file.write(output)
file.close()