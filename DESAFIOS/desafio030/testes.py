import hashlib

texto = "Coração"
cod = texto.encode('utf-8')
hash = hashlib.sha256(cod).hexdigest()


print(hash)


