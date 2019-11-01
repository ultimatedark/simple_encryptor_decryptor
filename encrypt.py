from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
class encryption_decryption:
    def __init__(self,message):
        self.message=message
    
    def encrypt(self):
        data = bytes(self.message)
        aad = b"authenticated but unencrypted data"
        key=ChaCha20Poly1305.generate_key()
        chacha = ChaCha20Poly1305(key)
        nonce=str(int(os.urandom(16).encode('hex'),16)) 
        ct = chacha.encrypt(nonce, data, aad)
        print(ct)
        return ct
 
    @staticmethod
    def decryptt(self):
        key=ChaCha20Poly1305.generate_key()
        aad = b"authenticated but unencrypted data"
        chacha = ChaCha20Poly1305(key)
        nonce=str(int(os.urandom(16).encode('hex'),16)) 
        return chacha.decrypt(nonce, encryption_decryption.encrypt(self), aad)


ab=encryption_decryption('dark penguin')

ab.encrypt()

