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
    
    def login(self, username, password):
        request = {
            "action": "login",
            "username": username,
            "password": password
        }
        
        response = self.send_request(request)
        
        if response and response.get("status") == "ok":
            self.token = response.get("token")
            self.authenticated = True
            print(f"\n[SUKSES] {response.get('message')}")
            print(f"[TOKEN] {self.token}")
            return True
        else:
            print(f"\n[GABIM] {response.get('message') if response else 'Gabim i panjohur'}")
            return False
    
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


def print_banner():
    print("=" * 50)
    print("KLIENTI JWT AUTHENTICATION")
    print("=" * 50)


def main():
    client = JWTClient()

    print_banner()

    print("\nDuke u lidhur me serverin...")
    if not client.connect():
        print("Nuk mund te vazhdohet pa lidhje me serverin.")
        return

    print("Lidhur me serverin!")

    while True:
        if not client.authenticated:
            print("\n" + "-" * 40)
            print("MENUJA E AUTENTIKIMIT")
            print("-" * 40)

            username = input("Username: ")
            password = getpass.getpass("Password: ")

            if client.login(username, password):
                print("\nAutentikim i suksesshem! Tani mund te aksesoni te dhenat e mbrojtura.")
            else:
                print("\nProvoni perseri.")
                continue

        print("\n" + "-" * 40)
        print("KOMANDAT E DISPONUESHME")
        print("-" * 40)
        print("   1  ->  get_data  - Merr te dhenat e mbrojtura")
        print("   2  ->  logout    - Shkycu")
        print("   3  ->  exit      - Dil nga aplikacioni")
        print("-" * 40)

        command = input("\nZgjedhja: ").strip().lower()

        if command == "1" or command == "get_data":
            client.get_protected_data()
        elif command == "2" or command == "logout":
            client.logout()
        elif command == "3" or command == "exit":
            print("\nDuke u mbyllur... Faleminderit!")
            break
        else:
            print("\nKomande e panjohur!")

    client.close()


if __name__ == "__main__":
    main()

