import yaml
import psycopg2
from psycopg2.extensions import AsIs

with open('./credentials', 'r') as credential_yaml:
    credentials = yaml.load(credential_yaml)

with open('./config', 'r') as config_yaml:
    config = yaml.load(config_yaml)
