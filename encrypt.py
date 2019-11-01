from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
class encryption_decryption:
    def __init__(self,message):
        self.message=message
    
    def encrypt(self):
        data = bytes(self.message,encoding="UTF-8")
        aad = b"authenticated but unencrypted data"
        key=ChaCha20Poly1305.generate_key()
        chacha = ChaCha20Poly1305(key)
        nonce=os.urandom(12) 
        ct = chacha.encrypt(nonce, data, aad)
        print(ct)
        return ct
 
    @staticmethod
    def decryptt(message):
        key=ChaCha20Poly1305.generate_key()
        aad = b"authenticated but unencrypted data"
        chacha = ChaCha20Poly1305(key)
        nonce=os.urandom(12) 
        return chacha.decrypt(nonce,bytes(message), aad)


ab=encryption_decryption('dark penguin')

a=ab.encrypt()
ab.decryptt(a)

