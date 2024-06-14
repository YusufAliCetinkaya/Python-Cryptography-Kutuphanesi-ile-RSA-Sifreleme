from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Anahtar çifti oluştur
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()

# Public key'i PEM formatında yazdır
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Public Key (PEM formatında):\n", public_pem.decode('utf-8'))

# Private key'i PEM formatında yazdır
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
print("Private Key (PEM formatında):\n", private_pem.decode('utf-8'))

# Şifrelenicek metin girişi
plaintext = input("Şifrelenecek metni girin: ")
plaintext_bytes = plaintext.encode('utf-8')  # String'i byte dizisine dönüştürme

# Encrypt
ciphertext = public_key.encrypt(
    plaintext_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Şifrelenmiş metin:", ciphertext.hex())
