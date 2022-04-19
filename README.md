# PANW Setup
A faster way to deploy Palo Alto Network firewalls. These modules interact with PAN-OS firewalls via the PAN Python SDK which you can read about here: https://panos.pan.dev/docs/apis/panpython_qs/

# Features
Quickly push configurations to Palo Alto Network firewalls including:
* Device configuration (hostname, domain, timezone, etc)
* Interface configuration
* Custom URL lists
* Security Rules
* Routing configuration
* Zone configuration

## Installation
```bash
# Clone this repository
$ git clone https://github.com/tylerdavidspangler/panw_setup.git

# Go into the repository
$ cd panw_setup

# Install dependencies
$ pip install -r requirements.txt
```

## CSV files

Before running the scripts, fill out the included CSV files. There are 6 of them, one for each of the configuration modules.
For example, fill out rules.csv to include your desired security ruleset.

## Running the Script
There are two options for running the included modules. You can run configure_firewall.py which itself runs all enabled modules, or you can run the individual modules directly.
```bash
# Run the primary script which runs all modules
$ python configure_firewall.py

# Or run individual modules independently of the primary script
$ python zone.py
```
With either option, you will be prompted to enter your target firewall hostname or IP, as well as your credentials.

## Configuration Options
By default, all modules are enabled inside of configure_firewall.py. Edit the bool_options() function in configure_firewall.py if you only want to run select modules. Setting any of the below settings to False will cause that module not to run when configure_firewall.py is executed. 
```bash

def bool_options():
	'''
	Set which configurations will be executed
	Example: Set 'zone_config_bol':False to bypass zone config
	'''

	return {
		'device_config_bol'             :True, #Set True if device level settings should be configured, False otherwise.
		'zone_config_bol'         	:True, #Set True if zones should be configured, False otherwise.
		'interface_config_bol'    	:True, #Set True if interfaces should be configured, False otherwise.
		'vr_config_bol'           	:True, #Set True if virtual routers should be configured, False otherwise.
		'url_config_bol'          	:True, #Set True if custom URL lists should be configured, False otherwise.
		'security_config_bol'     	:True, #Set True if security rules should be configured, False otherwise.
		'commit_bool'                   :True, #Set True if executed configurations should be committed to the device, False if configurations should only be staged.
			}
```
