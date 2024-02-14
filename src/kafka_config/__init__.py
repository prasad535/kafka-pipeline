import os

from dotenv import load_dotenv

# Load secrets from the .env file
load_dotenv()

## Cloud API related variables
API_KEY = os.getenv('API_KEY', None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY', None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER', None)
ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL', None)

## Schema Registry API variables
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY', None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET', None)

## Authentication related variables
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL', None)
SSL_MECHENISM = os.getenv('SSL_MECHENISM', None)

