from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from app.config import CASSANDRA_HOST, CASSANDRA_KEYSPACE
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from cassandra.cluster import NoHostAvailable

# Define a retry decorator for connecting to Cassandra
@retry(
    stop=stop_after_attempt(10),  # Retry up to 10 times
    wait=wait_exponential(multiplier=1, min=2, max=30),  # Exponential backoff: 2s, 4s, 8s, ..., up to 30s
    retry=retry_if_exception_type(NoHostAvailable)  # Retry on NoHostAvailable error
)
def connect_to_cassandra():
    cluster = Cluster([CASSANDRA_HOST])
    return cluster.connect()

# Connect to Cassandra with retry
try:
    session = connect_to_cassandra()
except NoHostAvailable as e:
    raise Exception(f"Failed to connect to Cassandra after retries: {e}")

# Create keyspace if it doesn't exist
session.execute(f"""
CREATE KEYSPACE IF NOT EXISTS {CASSANDRA_KEYSPACE}
WITH replication = {{'class':'SimpleStrategy','replication_factor':1}}
""")

# Set the keyspace
session.set_keyspace(CASSANDRA_KEYSPACE)

# Create table if it doesn't exist
session.execute(
    """ CREATE TABLE IF NOT EXISTS books(
    book_id TEXT PRIMARY KEY,
    title TEXT
    )
"""
)

def insert_book(book_id: str, title: str):
    session.execute(
        "INSERT INTO books(book_id,title) VALUES (%s,%s)", (book_id, title)
    )

def get_book(book_id: str):
    result = session.execute("SELECT * FROM books WHERE book_id=%s", (book_id,))
    return result.one()