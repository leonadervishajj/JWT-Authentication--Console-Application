import socket
import threading
import jwt
import json
from datetime import datetime, timedelta, timezone

HOST = "127.0.0.1"
PORT = 5000


USERS = {
    "jane_doe": "password123",
    "admin": "admin123"
}


def load_private_key():
    with open("keys/private.pem", "rb") as f:
        return f.read()

def load_public_key():
    with open("keys/public.pem", "rb") as f:
        return f.read()

PRIVATE_KEY = load_private_key()
PUBLIC_KEY = load_public_key()

def generate_jwt(username):
    """Gjeneron JWT për përdoruesin"""
    payload = {
        "username": username,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }
    token = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")
    return token

def verify_jwt(token):
    """Verifikon JWT dhe kthen payload-in nëse është valid"""
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
        return payload
    except:
        return None