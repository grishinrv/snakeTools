import os
import configparser
import shutil


def substitute_home_path(input_string):
    if input_string and input_string[0] == '~':
        return os.environ["HOME"] + input_string[1:]
    else:
        return input_string


def normalize_path(path):
    return os.path.normpath(str.replace(path, '\\', '/'))


config = configparser.ConfigParser()
config.read('./copier.config')
destination = normalize_path(substitute_home_path(config['destination']['path']))
print("Copying into: ", destination)
for key in config['paths']:
    shutil.copy(config['paths'][key], destination)
print('Copying job complete')