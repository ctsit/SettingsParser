import ConfigParser                                                                      
import StringIO
import os

section="NO_SECTION"
class settingsParser(ConfigParser.RawConfigParser):
                                             
    properties = {}
    required_options = set()

    def read_file(self,filename):
        if not os.path.exists(filename):
            raise Exception("Error: " + filename + " settings file not found at "
                           + filename)
        text = open(filename).read()
        f = StringIO.StringIO("[%s]\n" % section + text)
        self.readfp(f, filename)

    def get_option(self, option):
        'get the value of an option'
        try:
            opt_as_string = self.get(section, option)
        except:
            raise Exception('Option '+option+ ' not found in settings')
        return self.get_correct_type_value(self.properties.get(option),opt_as_string)

    def add_setting(self,option, type, required, defaultValue):
        self.properties[option] = type
        if required:
            self.required_options.add(option);

    # Need to discuss with teaber if this is required
    def set_option(option,value):
        option_type = properties.get(option)
        self.parser.set(self.section,option,get_correct_type_value(option_type,value))

    def get_correct_type_value(self,option_type,value):
        if value is None or value == "":
            return value
        if option_type == int:
            return int(value)
        elif option_type == long:
            return long(value)
        elif option_type == float:
            return float(value)
        elif option_type == bool:
            return bool(value)
        else:
            return value

    def get_options_list(self):
        'get a list of available options'
        return self.options(section)

    def get_user_settings(self):
        return list(self.properties.keys())

    def get_required_settings(self):
        return list(self.required_options)

    def has_option(self, option):
        """
        return True if an option is available, False otherwise.
        (NOTE: do not confuse with the original has_option)
        """
        return self.has_option(section, option)

    def check_required_field_configuration(self,filename):
        self.read_file(filename)
        for k in self.required_options:
            if self.get_option(k) is None or self.get_option(k) == "":
                raise Exception("required field \""+k+"\" not set")

# def main():                                                                        
#     parser = settingsParser()                                         
#     parser.add_setting("token",int,True,121212)
#     parser.add_setting("verify_ssl",bool,True,"true")
#     parser.add_setting("send_email",bool,True,"N")
#     # parser.check_required_field_configuration("settings2.ini")
#     print parser.get_required_settings()
#     print parser.get_user_settings()
    

if __name__ == "__main__":
    main()