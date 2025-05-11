import os 
from dotenv import load_dotenv

load_dotenv()

CASSANDRA_HOST = os.getenv("CASSANDRA_HOST")
CASSANDRA_KEYSPACE=os.getenv("CASSANDRA_KEYSPACE")

VALKEY_HOST = os.getenv("VALKEY_HOST")
VALKEY_PORT = int(os.getenv("VALKEY_PORT",6379))

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")