import rules
import interface
import list
import vr
import zone
import device
import fw

def bool_options():
	'''
	Set which configurations will be executed
	Example: Set 'zone_config_bol':False to bypass zone config
	'''

	return {
		'device_config_bol'			:True, #Set True if device level settings should be configured, False otherwise.
		'zone_config_bol'         	:True, #Set True if zones should be configured, False otherwise.
		'interface_config_bol'    	:True, #Set True if interfaces should be configured, False otherwise.
		'vr_config_bol'           	:True, #Set True if virtual routers should be configured, False otherwise.
		'url_config_bol'          	:True, #Set True if custom URL lists should be configured, False otherwise.
		'security_config_bol'     	:True, #Set True if security rules should be configured, False otherwise.
		'commit_bool'     			:True, #Set True if executed configurations should be commited to the device, False if configurations should only be staged.
			}

def configure_fw():

	'''
	Configures firewall with options as selected in above function (bool_options).
	For each configuration option which is set to True, this function calls a dedicated module which configures the firewall for that option.
	The parameters for these options are configured in the included CSV files which can be filled out as needed.
	Takes no input. Returns nothing. The called modules print status updates as they are run.
	Calls fw module, which will prompt user for target and credentials.
	'''

	#Pull boolean script options#
	options = bool_options()

	#Create firewall object#
	fw_object = fw.create()

	#Create device settings#
	if options['device_config_bol']==True:
		device.create_device_settings(fw_object)

	#Create zones#
	if options['zone_config_bol']==True:
		zone.create_zones(fw_object)

	#Create interfaces#
	if options['interface_config_bol']==True:
		interface.create_interfaces(fw_object)

	#Create VR#
	if options['vr_config_bol']==True:
		vr.create_vr(fw_object)

	#Create URL lists#
	if options['url_config_bol']==True:
		list.create_custom_lists(fw_object)

	#Create security rules#
	if options['security_config_bol']==True:
		rules.create_rules(fw_object)

	#Commit configuration#
	if options['commit_bool']==True:
		print("Proceeding to commit, this may take a few minutes...")
		commit_result = fw_object.commit(sync = True) #Sync option dictates script will wait until commit completion before proceeding.
		for message in commit_result['messages']: #Each message returned from firewall commit will be printed to console.
			print(message)

if __name__ == "__main__":
   configure_fw()