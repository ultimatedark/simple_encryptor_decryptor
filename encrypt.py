from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
import struct
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
        #print(ct)
        new_str=str(ct).split('\\x')
        #print(new_str)    
        print("".join(new_str))
        return ct

message=input("enter your message to encrypt:")
ab=encryption_decryption(message)

a=ab.encrypt()


