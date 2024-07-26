

from config import config

database_config = config['database']
logging_config = config['logging']
print(f"Database Host: {database_config['host']}")
print(f"Logging Level: {logging_config['level']}")

