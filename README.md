# JWT-Authentication--Console-Application

***Përshkrimi i Projektit**

Ky projekt implementon një sistem autentikimi dhe autorizimi duke përdorur JWT (JSON Web Token) në një arkitekturë Client-Server me Java.

Sistemi përbëhet nga dy aplikacione console:

Serveri – autentikon përdoruesit, gjeneron JWT token dhe kontrollon autorizimin.
Klienti – lidhet me serverin, dërgon kredencialet dhe përdor JWT token për të aksesuar resurset e mbrojtura.

Komunikimi ndërmjet client-it dhe serverit realizohet përmes Java Sockets (ServerSocket dhe Socket).

***Objektivat e Projektit**

Qëllimi kryesor i këtij projekti është:

- Të kuptohet funksionimi i JWT authentication.
- Të implementohet komunikimi Client-Server.
- Të realizohet autentikimi dhe autorizimi me token.
- Të implementohen protected endpoints.
- Të praktikohet programimi me Java sockets.
- Të kuptohet rëndësia e sigurisë në aplikacionet moderne.

***Arkitektura e Projektit**

***Flow i sistemit:***
   - Client lidhet me serverin.
   - Client dërgon username dhe password.
   - Serveri verifikon kredencialet.
   - Nëse login është valid:
   - serveri gjeneron JWT token.
   - Client ruan tokenin.
   - Për çdo protected request:
   - client dërgon JWT token.
   -  Serveri validon tokenin.
   - Nëse tokeni është valid:
   - serveri lejon qasjen në protected resource.

## Struktura e Projektit
JWT-Authentication-Console-Application/
-  server.py ***Serveri që pret lidhjet***
-  client.py ***Klienti për autentikim***
-  generate_keys.py ***Gjeneron çelësat RSA***
-  requirements.txt ***Varësitë e projektit***
-  README.md ***Dokumentacioni***
-  .gitignore ***File-t që injorohen nga Git***
-  keys/ ***Folderi i çelësave (gjenerohet automatikisht)***
-  private.pem ***Çelësi privat (vetëm serveri)***
-  public.pem ***Çelësi publik (për verifikim)***

***Shpjegimi i Klasave**
-  **server.py***
Kjo file përfaqëson serverin kryesor të aplikacionit.


***Funksionalitetet Kryesore***
- Krijon socket server duke përdorur:
***socket.socket()**
- Pret lidhje nga klientët.
- Menaxhon komunikimin Client-Server.
- Verifikon kredencialet e përdoruesit.
- Gjeneron JWT token pas login-it të suksesshëm.
- Validon JWT token për protected requests.
- Kthen përgjigje për klientin.
- Përgjegjësitë
- Authentication flow
- Authorization flow
- JWT validation
- Socket communication
- Error handling

**client.py***

Kjo file përfaqëson client application.

***Funksionalitetet Kryesore***
- Lidhet me serverin.
- Merr username dhe password nga përdoruesi.
- Dërgon login request.
- Merr JWT token nga serveri.
- Ruaj tokenin në memory.
- Dërgon protected requests.
- Menaxhon logout.
- Komandat e Disponueshme
***request_data**
***logout**
- Përgjegjësitë
- Client connection
- Request handling
- JWT storage
- User interaction


**generate_keys.py***

Kjo file përdoret për gjenerimin e RSA keys.

***Funksionalitetet Kryesore***
Gjeneron:
    private key
    public key
    Ruaj çelësat në:
    private.pem
    public.pem
    Përgjegjësitë
    RSA key generation
    Security setup

**private.pem***

Kjo file përmban RSA private key.

***Përdorimi***
- përdoret nga serveri për:
- JWT signing
- token generation
- Security

Private key:
1. nuk duhet të ndahet publikisht
2. përdoret vetëm nga serveri


**public.pem***

Kjo file përmban RSA public key.

***Përdorimi***
Përdoret për:
- JWT verification
- token validation
- Security

Public key:
mund të ndahet me klientët
nuk mund të përdoret për signing
requirements.txt

Kjo file përmban dependencies e projektit.


Instalimi realizohet me:
***pip install -r requirements.txt***


















- ***ClientHandler.java***

Kjo klasë menaxhon komunikimin me një klient specifik.

***Funksionet Kryesore***
- Lexon username/password.
- Verifikon login.
- Gjeneron JWT token.
- Validon tokenin.
- Menaxhon komandat:
- request_data
- logout
- Përgjegjësitë
- Authentication flow.
- Authorization flow.
- Error handling.

- ***JwtService.java***

Kjo klasë menaxhon krijimin dhe validimin e JWT tokenëve.

***Funksionet Kryesore***
- generateToken()
- Gjeneron JWT token duke përfshirë:
- username
- issued time (iat)
- expiration time (exp)
- validateToken()

***Kontrollon:***
- validitetin e tokenit
- expiration
- signature
- Përgjegjësitë
- Security logic.
- Token handling.

## Instalimi

### 1. Klonimi i repozitorit
```bash
git clone <repo-url>
cd JWT-Authentication-Console-Application
2. Instalimi i varësive
bash
pip install -r requirements.txt
3. Gjenerimi i çelësave RSA (vetëm një herë)
bash
python generate_keys.py
Ekzekutimi
Terminali 1 - Nis serverin
bash
python server.py
Terminali 2 - Nis klientin
bash
python client.py
Përdorimi
Kredencialet testuese
Username	Password
jane_doe	password123
admin	admin123

Komandat e klientit
Komanda	Përshkrimi
1 ose get_data	Merr të dhënat e mbrojtura
2 ose logout	Shkyçet
3 ose exit	Dil nga aplikacioni
Si funksionon?
Procesi i autentikimit:
- Klienti lidhet me serverin përmes socket
- Klienti dërgon username dhe password
- Serveri verifikon kredencialet
- Serveri gjeneron JWT me iat dhe exp
- Serveri e nënshkruan JWT me çelësin privat RSA
- Serveri ia dërgon JWT klientit
- Klienti e ruan JWT në memorie
- Procesi i aksesit në të dhëna të mbrojtura:
- Klienti dërgon JWT së bashku me kërkesën
- Serveri verifikon JWT me çelësin publik
- Nëse token është valid, serveri kthen të dhënat e mbrojtura
- Nëse token është invalid ose i skaduar, serveri kthen gabim 401

