import configparser
import os
import sys


class ConfigReader:

    @staticmethod
    def read_config(section, key):
        # root_dir = sys.path[0]
        root_dir = os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()
        try:
            config.read(root_dir + '/pytest.ini')
        except FileNotFoundError:
            raise FileNotFoundError("configuration file 'pytest.ini' not found")

        if config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")
