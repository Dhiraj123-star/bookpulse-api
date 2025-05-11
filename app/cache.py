import redis
from app.config import VALKEY_HOST,VALKEY_PORT

client = redis.Redis(host=VALKEY_HOST,port=VALKEY_PORT,decode_responses=True)

def get_cached_book(book_id:str):
    return client.get(book_id)

def set_cached_book(book_id:str,title:str,ttl:int=60):
    client.setex(book_id,ttl,title)

