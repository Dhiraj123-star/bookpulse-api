from cassandra.cluster import Cluster
from app.config import CASSANDRA_HOST, CASSANDRA_KEYSPACE
from passlib.context import CryptContext

# Connect to Cassandra (reuse existing session for simplicity)
from app.cassandra_db import session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(username: str):
    result = session.execute("SELECT * FROM users WHERE username=%s", (username,))
    return result.one()

def verify_user(username: str, password: str):
    user = get_user(username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def create_user(username: str, password: str):
    # Check if username exists
    if get_user(username):
        raise ValueError("Username already exists")
    hashed_password = pwd_context.hash(password)
    session.execute(
        "INSERT INTO users (username, hashed_password) VALUES (%s, %s)",
        (username, hashed_password)
    )