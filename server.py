import socket
import threading
from xmlrpc import server
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
    
def handle_client(client_socket, address):
    print(f"[LIDHJE] {address} u lidh")
    
    while True:
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                break
            
            request = json.loads(data)
            action = request.get("action")
            
           
            if action == "login":
                username = request.get("username")
                password = request.get("password")
                
                print(f"[AUTH] Përpjekje për login nga {username}")
                
                if username in USERS and USERS[username] == password:
                    token = generate_jwt(username)
                    response = {
                        "status": "ok",
                        "message": "Autentikimi u krye me sukses",
                        "token": token
                    }
                    print(f"[SUKSES] {username} u autentikua")
                else:
                    response = {
                        "status": "error",
                        "message": "Username ose password i gabuar"
                    }
                    print(f"[DËSHTIM] {username} deshti")
                
                client_socket.send(json.dumps(response).encode('utf-8'))
            
       
            elif action == "get_data":
                token = request.get("token")
                
                if not token:
                    response = {
                        "status": "error",
                        "message": "Nuk jeni të autentikuar. Ju lutem logohuni fillimisht."
                    }
                else:
                    payload = verify_jwt(token)
                    if payload:
                        response = {
                            "status": "ok",
                            "data": {
                                "message": "Këto janë të dhënat e mbrojtura!",
                                "secret": "Kodi sekret është: 12345",
                                "timestamp": datetime.now().isoformat(),
                                "user": payload.get("username")
                            }
                        }
                        print(f"[AKSES] {payload.get('username')} mori të dhënat e mbrojtura")
                    else:
                        response = {
                            "status": "error",
                            "message": "Token i skaduar ose i pavlefshëm. Ju lutem logohuni përsëri."
                        }
                        print(f"[REFUZIM] Tentim aksesi me token të pavlefshëm")
                
                client_socket.send(json.dumps(response).encode('utf-8'))
            
            else:
                response = {"status": "error", "message": "Komandë e panjohur"}
                client_socket.send(json.dumps(response).encode('utf-8'))
                
        except Exception as e:
            print(f"[GABIM] {e}")
            break
    
    client_socket.close()
    print(f"[SHKËPUTJE] {address} u shkëput")
    
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print("=" * 60)
    print("SERVERI JWT PO PUNON")
    print(f"Host: {HOST}")
    print(f"Port: {PORT}")
    print("Duke pritur per lidhje...")
    print("=" * 60)
    
    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    main()