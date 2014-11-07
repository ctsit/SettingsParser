# Settings Parser

The settingsParser is a wrapper for the ConfigParser module available in python. 

1) This parser allows users to parse .ini files without any sections defined in it.

2) It allows users to add expected fields and required fields in the settings file.

3) It allows users to check if the required fields are set in the settings file.

# Usage

## Add fields:

Fields can be added by using the method `add_setting` as shown below.

`
		
		parser = settingsParser.settingsParser()
		
		parser.add_setting("testkey_1",int,False,123)
		
		parser.add_setting("testkey_2",bool,False,"true")
		
		parser.add_setting("testkey_3",bool,False,"N")
        
`

## Add required fields:

Required Fields can be added by passing True to the third argument for the method `add_setting` as shown below.

`

		parser = settingsParser.settingsParser()
		
		parser.add_setting("testkey_1",int,True,123)
		
		parser.add_setting("testkey_2",bool,True,"true")
		
		parser.add_setting("testkey_3",bool,True,"N")

`

## Get Fields:

One can read values set for fields by using the method `get_option` as shown below.

`
Consider below settings.ini as an example

Settings.ini

server_name = "http://fakeserver.com/"

server_port = 88

	parser = settingsParser.settingsParser()
	parser.read_file(Settings.ini)
	parser.getoption("server_name")
		

`


## Validate required fields:

We can check the whether the required fields are set or not by calling the function `check_required_field_configuration` as shown below.

`
	
		parser = settingsParser.settingsParser()
		
		parser.add_setting("testkey_1",int,True,123)
		
		parser.add_setting("testkey_2",bool,True,"true")
		
		parser.add_setting("testkey_3",bool,True,"N")
		
		parser.check_required_field_configuration("settings.ini")

`

This method takes the complete path of the settings.ini file as argument and checks if the fields set as required are passed in the settings.ini or not.


## Get User Settings:

For retrieving the settings set by the user one can use `get_user_settings` method as shown below.

`
	
		parser = settingsParser.settingsParser()
        parser.add_setting("testkey_1",int,True,123)
        parser.add_setting("testkey_2",bool,False,"true")
        parser.add_setting("testkey_3",bool,True,"N")
        
        
        ... some code...
        
        
        parser.get_user_settings() 
        
        // this returns the list of settings added by the user. In our example here it returns a list containing "testkey_1", "testkey_2", "testkey_3".

`

## Get Required Settings:

For retrieving only the required fields set by the user one can use `get_required_settings` as shown below.

`

		parser = settingsParser.settingsParser()
        parser.add_setting("testkey_1",int,True,123)
        parser.add_setting("testkey_2",bool,False,"true")
        parser.add_setting("testkey_3",bool,True,"N")
        
        ... some code...
        
        
		parser.get_required_settings()
		
		// this returns the list of required fields added by the user. In our example here it returns a list containing "testkey_1", "testkey_3".				

`

# Running Test cases:

For running test cases for the settingsParser module, one can run the command `python TestParser.py` from the root directory on the command line.


