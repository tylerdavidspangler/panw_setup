from panos.objects import CustomUrlCategory
import fw
import csv

def create_custom_lists(fw):

	'''
	Takes firewall object as input. Creates custom URL lists on Palo Alto Firewall.
	Included parameters: list name, list description, list type, list URL values
	Parameters set in the csv file at csv/list.csv
	'''

	url_file = "csv/list.csv"
	file_ = open(url_file, 'r')
	csv_reader = csv.reader(file_)

	for row in csv_reader:
		list_name       				= row[0]
		list_description       			= row[1]
		list_type         				= row[2]
		list_url_values         		= row[3].split(" ")

		list = CustomUrlCategory(name = list_name, description = list_description, type = list_type, url_value = list_url_values)
		fw.add(list)
		list.create()
	
	print('Custom Lists Creation...Complete')

if __name__ == "__main__":
   create_custom_lists(fw.create())