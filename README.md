# Python-Cryptography-Kutuphanesi-ile-RSA-Sifreleme

Tabii, işte bu projeye uygun bir README metni örneği:

---

# RSA Şifreleme

Bu proje, Python'un `cryptography` kütüphanesi kullanılarak RSA algoritması ile metin şifreleme işlemlerini göstermektedir.

## Gereksinimler

Projenin çalışması için Python3 ve `cryptography` kütüphanesinin yüklü olması gerekmektedir. `cryptography` kütüphanesini yüklemek için terminal veya komut istemcisinde şu komutu kullanabilirsiniz:

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
