import os
import configparser
import shutil


def substitute_home_path(input_string):
    if input_string and input_string[0] == '~':
        return os.environ["HOME"] + input_string[1:]
    else:
        return input_string


config = configparser.ConfigParser()
config.read('./copier.config')
destination = substitute_home_path(config['destination']['path'])
for key in config['paths']:
    shutil.copy(config['paths'][key], destination)
print('Copying job complete')