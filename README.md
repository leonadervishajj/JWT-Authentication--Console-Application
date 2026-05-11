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

