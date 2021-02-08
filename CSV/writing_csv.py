import csv

with open('network_inventory.csv', mode='w') as device_file:
    device_writer = csv.writer(device_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    device_writer.writerow(['Hostname', 'IP', 'Username', 'Password', 'Secret', 'OS'])
    device_writer.writerow(['R2', '192.168.101.133', 'cisco', 'cisco', 'cisco', 'ios'])
    device_writer.writerow(['R3', '192.168.101.134', 'cisco', 'cisco', 'cisco', 'ios'])
    device_writer.writerow(['R4', '192.168.101.135', 'cisco', 'cisco', 'cisco', 'ios'])
