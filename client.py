import socket
import json
import getpass

HOST = "127.0.0.1"
PORT = 5000

class JWTClient:
    def __init__(self):
        self.socket = None
        self.token = None
        self.authenticated = False
    
    def connect(self):
        """Lidhet me serverin"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((HOST, PORT))
            return True
        except Exception as e:
            print(f"[GABIM] Nuk mund te lidhej me serverin: {e}")
            return False
    
    def send_request(self, request):
        """Dergon kerkese ne server dhe kthen pergjigjen"""
        try:
            self.socket.send(json.dumps(request).encode('utf-8'))
            response = self.socket.recv(4096).decode('utf-8')
            return json.loads(response)
        except Exception as e:
            print(f"[GABIM] Gabim ne komunikim: {e}")
            return None
    
    def close(self):
        """Mbylle lidhjen me serverin"""
        if self.socket:
            self.socket.close()

def get_protected_data(self):
        """Merr te dhena te mbrojtura nga serveri"""
        if not self.token:
            print("\n[GABIM] Nuk jeni te autentikuar! Ju lutem logohuni fillimisht.")
            return None
       
        request = {
            "action": "get_data",
            "token": self.token
        }
       
        response = self.send_request(request)
       
        if response and response.get("status") == "ok":
            data = response.get("data")
            print("\n" + "=" * 50)
            print("TE DHENAT E MBROJTURA:")
            print(f"  Message: {data.get('message')}")
            print(f"  Secret: {data.get('secret')}")
            print(f"  User: {data.get('user')}")
            print(f"  Timestamp: {data.get('timestamp')}")
            print("=" * 50)
            return data
        else:
            print(f"\n[GABIM] {response.get('message') if response else 'Gabim i panjohur'}")
            return None
   
            def logout(self):
             """Shkyqet dhe fshin token-in"""
        self.token = None
        self.authenticated = False
        print("\n[LOGOUT] Jeni shkyqur me sukses!")
