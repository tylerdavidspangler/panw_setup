from panos.network import Zone
import fw
import csv

def create_zones(fw):

	'''
	Takes firewall object as input. Creates zones on Palo Alto Firewall.
	Included parameters: zone name, zone type
	Parameters set in the csv file at csv/zone.csv
	'''

	zone_file = "csv/zone.csv"
	file_ = open(zone_file, 'r')
	csv_reader = csv.reader(file_)

	for row in csv_reader:
		zone       = row[0]
		type       = row[1]
		
		zone_object = Zone(zone, type)
		fw.add(zone_object)
		zone_object.create()

	print('Zone Creation...Complete')

if __name__ == "__main__":
   create_zones(fw.create())