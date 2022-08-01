from Cryptodome.Cipher import AES
import base64
import hashlib
class PrpCrypt(object):
    def __init__(self, key):
        self.key = bytes.fromhex(key)
        self.mode = AES.MODE_CBC
        self.iv = hashlib.md5('1615528982'.encode('utf-8')).digest()

    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.iv)
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\01' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\01' * add).encode('utf-8')
        a=cryptor.encrypt(text)
        self.ciphertext = self.iv+a
        return str(base64.b64encode(self.ciphertext),'utf-8')

    def decrypt(self, text):
        iv = base64.b64decode(text)[0:16]
        encry_text = base64.b64decode(text)[16:]
        cryptor = AES.new(self.key, self.mode, iv)
        plain_text = cryptor.decrypt(encry_text)
        return str(plain_text, 'utf-8').rstrip('\01')
key=hashlib.md5(('b831381d-6324-4d53-ad4f-8cda48b30811'+'c48619fe-8f02-49e0-b9e9-edf763e17e21').encode('utf-8')).hexdigest()
print("key:",key)   
pc = PrpCrypt(key)
text = ''
print(pc.encrypt(text))