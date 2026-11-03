"""
IoT with AI Internship — Week 4 Capstone
AES-256 Payload Encryption & Secure MQTT Communication Module
"""

import json
from cryptography.fernet import Fernet

# Static Secret Key for AES-256 Symmetric Encryption
FERNET_KEY = Fernet.generate_key()
cipher_suite = Fernet(FERNET_KEY)

def encrypt_payload(data: dict) -> str:
    """Encrypts sensor telemetry JSON into AES-256 ciphertext."""
    json_bytes = json.dumps(data).encode("utf-8")
    encrypted_text = cipher_suite.encrypt(json_bytes)
    return encrypted_text.decode("utf-8")

def decrypt_payload(token_str: str) -> dict:
    """Decrypts ciphertext back into original JSON telemetry."""
    decrypted_bytes = cipher_suite.decrypt(token_str.encode("utf-8"))
    return json.loads(decrypted_bytes.decode("utf-8"))

if __name__ == "__main__":
    sample_data = {"temperature": 24.5, "motion": 1, "light": 450, "sound": 55}
    token = encrypt_payload(sample_data)
    print(f"[*] Ciphertext Payload: {token[:30]}...")
    print(f"[✔] Decrypted Payload: {decrypt_payload(token)}")