from panos.policies import Rulebase
from panos.policies import SecurityRule
import fw
import csv

def create_rules(fw):

	'''
	Takes firewall object as input. Creates security rules on Palo Alto Firewall.
	Rule parameters are set in the csv file at csv/rules.csv
	Included settings for each rule in the order they appear in the csv:
	Rule name, source zone, source ip, destination ip, application, service, action
	'''

	rulebase = Rulebase()
	fw.add(rulebase)
	rule_file = "csv/rules.csv"
	file_ = open(rule_file, 'r')
	csv_reader = csv.reader(file_)

	for row in csv_reader:
		rule_name         = row[0]
		source_zone       = row[1].split(" ")
		source_ip         = row[2].split(" ")   
		destination_zone  = row[3].split(" ")    
		destination_ip    = row[4].split(" ")    
		application       = row[5].split(" ")    
		service           = row[6].split(" ")   
		action            = row[7]

		security_rule = SecurityRule(name=rule_name, fromzone=source_zone, source=source_ip, tozone=destination_zone,  destination=destination_ip, application=application, service=service, action=action)
		rulebase.add(security_rule)
		security_rule.create()
		
	print("Security Rule Creation... Complete")

if __name__ == "__main__":
   create_rules(fw.create())