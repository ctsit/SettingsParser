import unittest
from lxml import etree
import os
import settingsParser
import tempfile

class TestParser(unittest.TestCase):

    def setUp(self):
        self.settings = tempfile.NamedTemporaryFile()
        self.settings.write("""testkey_1 = 121212
testkey_2 = true
testkey_3 = 
""")
        self.settings.seek(0)
        return()


    def test_check_required_field_configuration(self):
        parser = settingsParser.settingsParser()
        parser.add_setting("testkey_1",int,True,121212)
        parser.add_setting("testkey_2",bool,False,"true")
        parser.add_setting("testkey_3",bool,True,"N")
        self.assertRaises(Exception, parser.check_required_field_configuration,self.settings.name)


    def test_get_correct_type_value(self):
        parser = settingsParser.settingsParser()
        if parser.get_correct_type_value(int,1212) == 1212:
            pass
        if parser.get_correct_type_value(float,1212) == 1212.0:
            pass
        if parser.get_correct_type_value(bool,True) == True:
            pass
        if parser.get_correct_type_value(int,"") == "":
            pass

    def test_get_option(self):
        parser = settingsParser.settingsParser()
        parser.add_setting("testkey_1",int,True,121212)
        parser.add_setting("testkey_2",bool,False,"true")
        parser.add_setting("testkey_3",bool,True,"N")
        parser.read_file(self.settings.name)
        self.assertEqual(121212,parser.get_option("testkey_1"))
        self.assertRaises(Exception, parser.get_option,"testkey_4")

    def test_get_user_settings(self):
        parser = settingsParser.settingsParser()
        parser.add_setting("testkey_1",int,True,121212)
        parser.add_setting("testkey_2",bool,False,"true")
        parser.add_setting("testkey_3",bool,True,"N")
        self.assertListEqual(["testkey_1","testkey_3","testkey_2"],parser.get_user_settings())

    def test_get_required_settings(self):
        parser = settingsParser.settingsParser()
        parser.add_setting("testkey_1",int,True,121212)
        parser.add_setting("testkey_2",bool,False,"true")
        parser.add_setting("testkey_3",bool,True,"N")
        self.assertListEqual(["testkey_1","testkey_3"],parser.get_required_settings())

    def tearDown(self):
        self.settings.close()
        return()

if __name__ == '__main__':
    unittest.main()
