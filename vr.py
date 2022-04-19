from panos.network import VirtualRouter
import fw
import csv

def create_vr(fw):

	'''
	Takes firewall object as input. Creates virtual routers on Palo Alto Firewall.
	Included parameters: virtual router name, virtual router interfaces
	Parameters set in the csv file at csv/vr.csv
	'''

	vr_file = "csv/vr.csv"
	file_ = open(vr_file, 'r')
	csv_reader = csv.reader(file_)

	for row in csv_reader:
		vr_name       		= row[0]
		vr_interfaces       = row[1].split(" ")

		vr_instance = VirtualRouter(vr_name, vr_interfaces)
		fw.add(vr_instance)
		vr_instance.create()
	
	print('VR Creation...Complete')

if __name__ == "__main__":
   create_vr(fw.create())