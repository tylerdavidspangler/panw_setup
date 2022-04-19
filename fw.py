from panos.firewall import Firewall
from getpass import getpass

def create():

	'''Prompts user to enter credentials. Returns firewall object that is needed for other modules.'''

	#Prompt user for credentials#
	ip = input("Firewall IP or URL: ")
	username = input("Username: ")
	password = getpass()
	
	#Create firewall object#
	fw = Firewall(ip, username, password)
	return fw