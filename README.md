# Python-Cryptography-Kutuphanesi-ile-RSA-Sifreleme

Tabii, işte bu projeye uygun bir README metni örneği:

---

# RSA Şifreleme ve Deşifreleme Örneği

Bu proje, Python'un `cryptography` kütüphanesi kullanılarak RSA algoritması ile metin şifreleme ve deşifreleme işlemlerini göstermektedir.

## Gereksinimler

Projenin çalışması için Python 3 ve `cryptography` kütüphanesinin yüklü olması gerekmektedir. `cryptography` kütüphanesini yüklemek için terminal veya komut istemcisinde şu komutu kullanabilirsiniz:

```
pip install cryptography
```

## Kullanım

1. **Anahtar Çifti Oluşturma:**

   - Proje başlangıcında, `rsa.generate_private_key()` fonksiyonu ile RSA algoritmasına uygun bir özel anahtar (private key) çifti oluşturulur.
   - Oluşturulan özel anahtarın genel anahtarı (public key) elde edilir.

2. **Metin Şifreleme:**

   - Kullanıcıdan şifrelenecek metin girdisi alınır.
   - `public_key.encrypt()` metodu ile metin, genel anahtar (public key) kullanılarak RSA algoritması ile şifrelenir.

3. **Şifrelenmiş Metni Kullanma:**

   - Şifrelenmiş metin, byte dizisi veya hex formatında elde edilir. Bu şekilde güvenli iletim veya depolama sağlanabilir.

## Örnek Kod

```python
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

# Kullanıcıdan şifrelenecek metni al
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
```
