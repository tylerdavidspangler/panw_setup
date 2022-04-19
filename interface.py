from panos.network import EthernetInterface
import fw
import csv

def create_interfaces(fw):

	'''
	Takes firewall object as input. Creates interface level settings on Palo Alto Firewall.
	Included settings: interface name, interface mode, dhcp enabled setting (bool)
	Values for these settings are set in the csv file at csv/interface.csv
	'''

	interface_file = "csv/interface.csv"
	file_ = open(interface_file, 'r')
	csv_reader = csv.reader(file_)

	for row in csv_reader:
		int_name       			= row[0]
		int_mode       			= row[1]
		enable_dhcp_bol         = row[2]

		eth_instance = EthernetInterface(name = int_name, mode = int_mode, enable_dhcp = enable_dhcp_bol)
		fw.add(eth_instance)
		eth_instance.create()

	print('Interface Creation...Complete')
	
if __name__ == "__main__":
   create_interfaces(fw.create())