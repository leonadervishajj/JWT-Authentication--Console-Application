# JWT-Authentication--Console-Application

# JWT Authentication Console Application

## Përshkrimi
Ky është një sistem autentikimi JWT (JSON Web Token) me arkitekturë client-server duke përdorur socket komunikim. Serveri autentikon kredencialet e dërguara nga klienti dhe, pas autentikimit të suksesshëm, lëshon një JWT për qasje në burimet e mbrojtura.

## Teknologjitë
- Python 3.x
- Socket për komunikim client-server
- JWT me RSA (algoritmi asimetrik RS256)
- PyJWT për manipulimin e JWT
- Cryptography për gjenerimin e çelësave RSA

## Struktura e Projektit
JWT-Authentication-Console-Application/
-  server.py # Serveri që pret lidhjet
-  client.py # Klienti për autentikim
-  generate_keys.py # Gjeneron çelësat RSA
-  requirements.txt # Varësitë e projektit
-  README.md # Dokumentacioni
-  .gitignore # File-t që injorohen nga Git
-  keys/ # Folderi i çelësave (gjenerohet automatikisht)
-  private.pem # Çelësi privat (vetëm serveri)
-  public.pem # Çelësi publik (për verifikim)


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

