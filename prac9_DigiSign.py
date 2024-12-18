import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def create_digital_signature(data, private_key):
    rsa_key = RSA.import_key(private_key)
    h = SHA256.new(data)
    signature = pkcs1_15.new(rsa_key).sign(h)
    return signature

def verify_digital_signature(data, signature, public_key):
    rsa_key = RSA.import_key(public_key)
    h = SHA256.new(data)
    try:
        pkcs1_15.new(rsa_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    input_data = b"Attack On Titans"
    private_key, public_key = generate_rsa_keypair()
    signature = create_digital_signature(input_data, private_key)
    print(f"Signature Value:\n {base64.b64encode(signature).decode()}")
    verification = verify_digital_signature(input_data, signature, public_key)
    print(f"Verification: {verification}")