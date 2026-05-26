import base64

def encrypt_data(source_text: str, key_string: str) -> str:
    data_bytes = source_text.encode('utf-8')
    key_bytes = key_string.encode('utf-8')
    
    encrypted_bytes = bytearray()
    for i, byte in enumerate(data_bytes):
        key_byte = key_bytes[i % len(key_bytes)]
        encrypted_bytes.append(byte ^ key_byte)
        
    return base64.b64encode(encrypted_bytes).decode('utf-8')


def decrypt_data(base64_text: str, key_string: str) -> str:
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    key_bytes = key_string.encode('utf-8')
    
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        key_byte = key_bytes[i % len(key_bytes)]
        decrypted_bytes.append(byte ^ key_byte)
        
    return decrypted_bytes.decode('utf-8')
