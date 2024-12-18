from Crypto.Util.number import inverse, getPrime, bytes_to_long, long_to_bytes

class RSA_PKCS7:
    def __init__(self, key_size=512):
        self.key_size = key_size
        self.block_size = (key_size // 8) - 11 

    def generate_keys(self):
        a = getPrime(self.key_size // 2)
        b = getPrime(self.key_size // 2)
        n = a * b
        phi_n = (a - 1) * (b - 1)
        e = 65537
        d = inverse(e, phi_n)
        return (n, e), (n, d) 

    def pkcs7_pad(self, data, block_size):
        data_bytes = data.encode('utf-8')
        pad_length = block_size - len(data_bytes) % block_size
        padding = bytes([pad_length] * pad_length)
        return data_bytes + padding

    def pkcs7_unpad(self, data_bytes):
        pad_length = data_bytes[-1]
        return data_bytes[:-pad_length].decode('utf-8')
    
    def encrypt(self, plaintext, public_key):
        n, e = public_key
        padded_data = self.pkcs7_pad(plaintext, self.block_size)
        encrypted_chunks = []
        for i in range(0, len(padded_data), self.block_size):
            chunk = padded_data[i:i + self.block_size]
            chunk_int = bytes_to_long(chunk)
            encrypted_chunk = pow(chunk_int, e, n)
            encrypted_chunks.append(encrypted_chunk)
        return encrypted_chunks

    def decrypt(self, encrypted_chunks, private_key):
        n, d = private_key
        decrypted_data = b""
        for chunk in encrypted_chunks:
            decrypted_int = pow(chunk, d, n)
            decrypted_chunk = long_to_bytes(decrypted_int, self.block_size)
            decrypted_data += decrypted_chunk
        return self.pkcs7_unpad(decrypted_data)

rsa = RSA_PKCS7()
public_key, private_key = rsa.generate_keys()

plaintext = "Demon Slayer."
print("Plaintext:", plaintext)
encrypted_chunks = rsa.encrypt(plaintext, public_key)
print("Encrypted text:", encrypted_chunks[0])
decrypted_text = rsa.decrypt(encrypted_chunks, private_key)
print("Decrypted text:", decrypted_text)
