import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


if not os.path.exists("keys"):
    os.makedirs("keys")


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)


with open("keys/private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))


public_key = private_key.public_key()


with open("keys/public.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print(" Çelësat u krijuan me sukses në folderin 'keys'")
print("   - keys/private.pem")
print("   - keys/public.pem")