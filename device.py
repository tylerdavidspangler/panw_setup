from panos.device import SystemSettings
import fw
import csv

def create_device_settings(fw):

	'''
	Takes firewall object as input. Creates device level settings on Palo Alto Firewall.
	Included settings: hostname, domain, timezone
	Values for these settings are set in the csv file at csv/device.csv
	'''

	device_file = "csv/device.csv"
	file_ = open(device_file, 'r')
	csv_reader = csv.reader(file_)

	for row in csv_reader:
		device_hostname       			= row[0]
		device_domain       			= row[1]
		device_timezone         		= row[2]

		sysset = SystemSettings(hostname = device_hostname, domain = device_domain, timezone = device_timezone)
		fw.add(sysset)
		sysset.create()
	
	print('Device Settings Creation...Complete')

if __name__ == "__main__":
   create_device_settings(fw.create())