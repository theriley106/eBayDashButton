import os

if __name__ == "__main__":
	if os.path.isfile("amazon-dash.yml") == False:
		print("You haven't created a valid config file yet...")
		if raw_input("Create one now? Y/N ").upper() == "Y":
			mac = raw_input("Dash Button Mac Address: ")
			delay = raw_input("Delay between button press: ")
			itemNum = raw_input("Item Number: ")
			file = open("amazon-dash.yml", "w")
			'''
			settings:
			  delay: {}
			devices:
			  {}:
			    name: test
			    user: test
			    cmd: python controller.py {}
			    '''.format(delay, mac, itemNum)
			file.write(config) 
			file.close()
			os.system("sudo chown root:root amazon-dash.yml")
			os.system("sudo chmod 700 amazon-dash.yml")
	try:
		os.system("sudo amazon-dash run")
	except:
		Exception('It looks like you don\'t have Amazon Dash Installed - run "sudo pip install amazon-dash"')
			