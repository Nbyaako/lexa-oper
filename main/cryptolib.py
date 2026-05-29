import base64
import hashlib
import math

def xor_encrypt(source_text: str, key_string: str) -> str:
    data_bytes = source_text.encode('utf-8')
    key_bytes = key_string.encode('utf-8')
    
    encrypted_bytes = bytearray()
    for i, byte in enumerate(data_bytes):
        key_byte = key_bytes[i % len(key_bytes)]
        encrypted_bytes.append(byte ^ key_byte)
        
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def xor_decrypt(base64_text: str, key_string: str) -> str:
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    key_bytes = key_string.encode('utf-8')
    
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        key_byte = key_bytes[i % len(key_bytes)]
        decrypted_bytes.append(byte ^ key_byte)
        
    return decrypted_bytes.decode('utf-8')

def caesar_encrypt(source_text: str, key_string: str) -> str:
    shift = sum(ord(c) for c in key_string) % 256
    encrypted_bytes = bytearray()
    for byte in source_text.encode('utf-8'):
        encrypted_bytes.append((byte + shift) % 256)
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def caesar_decrypt(base64_text: str, key_string: str) -> str:
    shift = sum(ord(c) for c in key_string) % 256
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    decrypted_bytes = bytearray()
    for byte in encrypted_bytes:
        decrypted_bytes.append((byte - shift) % 256)
    return decrypted_bytes.decode('utf-8')


def vigenere_encrypt(source_text: str, key_string: str) -> str:
    key_hash = hashlib.sha256(key_string.encode()).digest()
    data_bytes = source_text.encode('utf-8')
    encrypted_bytes = bytearray()
    for i, byte in enumerate(data_bytes):
        key_byte = key_hash[i % len(key_hash)]
        encrypted_bytes.append((byte + key_byte) % 256)
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def vigenere_decrypt(base64_text: str, key_string: str) -> str:
    key_hash = hashlib.sha256(key_string.encode()).digest()
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        key_byte = key_hash[i % len(key_hash)]
        decrypted_bytes.append((byte - key_byte) % 256)
    return decrypted_bytes.decode('utf-8')


def des_encrypt(source_text: str, key_string: str) -> str:
    key_hash = hashlib.sha256(key_string.encode()).hexdigest()[:16]
    data_bytes = source_text.encode('utf-8')
    encrypted_bytes = bytearray()
    for i, byte in enumerate(data_bytes):
        key_byte = ord(key_hash[i % len(key_hash)])
        encrypted_bytes.append((byte ^ key_byte) + (i % 256))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def des_decrypt(base64_text: str, key_string: str) -> str:
    key_hash = hashlib.sha256(key_string.encode()).hexdigest()[:16]
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        key_byte = ord(key_hash[i % len(key_hash)])
        decrypted_bytes.append((byte - (i % 256)) ^ key_byte)
    return decrypted_bytes.decode('utf-8')


def blowfish_encrypt(source_text: str, key_string: str) -> str:
    key_hash = hashlib.blake2b(key_string.encode(), digest_size=32).digest()
    data_bytes = source_text.encode('utf-8')
    encrypted_bytes = bytearray()
    for i, byte in enumerate(data_bytes):
        key_byte = key_hash[i % len(key_hash)]
        encrypted_bytes.append((byte + key_byte * 7) % 256)
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def blowfish_decrypt(base64_text: str, key_string: str) -> str:
    key_hash = hashlib.blake2b(key_string.encode(), digest_size=32).digest()
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        key_byte = key_hash[i % len(key_hash)]
        decrypted_bytes.append((byte - key_byte * 7) % 256)
    return decrypted_bytes.decode('utf-8')

def twofish_encrypt(source_text: str, key_string: str) -> str:
    key_hash = hashlib.sha512(key_string.encode()).digest()
    data_bytes = source_text.encode('utf-8')
    encrypted_bytes = bytearray()
    for i, byte in enumerate(data_bytes):
        key_byte = key_hash[i % len(key_hash)]
        encrypted_bytes.append(((byte ^ key_byte) + 45) % 256)
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def twofish_decrypt(base64_text: str, key_string: str) -> str:
    key_hash = hashlib.sha512(key_string.encode()).digest()
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        key_byte = key_hash[i % len(key_hash)]
        decrypted_bytes.append(((byte - 45) % 256) ^ key_byte)
    return decrypted_bytes.decode('utf-8')

def serpent_encrypt(source_text: str, key_string: str) -> str:
    key_hash = hashlib.md5(key_string.encode()).digest()
    data_bytes = source_text.encode('utf-8')
    encrypted_bytes = bytearray()
    for i, byte in enumerate(data_bytes):
        key_byte = key_hash[i % len(key_hash)]
        encrypted_bytes.append(((byte * 13 + key_byte) ^ 0xAA) % 256)
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def serpent_decrypt(base64_text: str, key_string: str) -> str:
    key_hash = hashlib.md5(key_string.encode()).digest()
    encrypted_bytes = base64.b64decode(base64_text.encode('utf-8'))
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        key_byte = key_hash[i % len(key_hash)]
        decrypted_bytes.append((((byte ^ 0xAA) - key_byte) * 197) % 256)
    return decrypted_bytes.decode('utf-8')

def _extended_gcd(a: int, b: int):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = _extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def _mod_inverse(e: int, phi: int) -> int:
    gcd, x, _ = _extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Модульный обратный не существует")
    return (x % phi + phi) % phi

def _is_prime(n: int, k: int = 5) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(k):
        a = 2 + (int.from_bytes(hashlib.sha256(str(_).encode()).digest(), 'big') % (n - 3))
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def _generate_prime(seed: int, bits: int) -> int:
    counter = 0
    while True:
        candidate = int.from_bytes(
            hashlib.sha256((str(seed) + str(counter)).encode()).digest(), 'big'
        ) | (1 << bits - 1) | 1
        if _is_prime(candidate):
            return candidate
        counter += 1

def rsa_encrypt(source_text: str, key_string: str) -> str:
    hash_value = int(hashlib.sha256(key_string.encode()).hexdigest(), 16)
    
    p = _generate_prime(hash_value, 128)
    q = _generate_prime(hash_value + 1, 128)
    
    while p == q:
        q = _generate_prime(hash_value + 2, 128)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
    
    encrypted_numbers = []
    for char in source_text:
        m = ord(char)
        c = pow(m, e, n)
        encrypted_numbers.append(str(c))
    
    result = ','.join(encrypted_numbers)
    return base64.b64encode(result.encode()).decode('utf-8')

def rsa_decrypt(base64_text: str, key_string: str) -> str:
    hash_value = int(hashlib.sha256(key_string.encode()).hexdigest(), 16)
    
    p = _generate_prime(hash_value, 128)
    q = _generate_prime(hash_value + 1, 128)
    
    while p == q:
        q = _generate_prime(hash_value + 2, 128)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
    
    d = _mod_inverse(e, phi)
    
    result = base64.b64decode(base64_text.encode()).decode('utf-8')
    encrypted_numbers = result.split(',')
    
    decrypted_text = []
    for c_str in encrypted_numbers:
        try:
            c = int(c_str)
            m = pow(c, d, n)
            decrypted_text.append(chr(m))
        except (ValueError, OverflowError):
            pass
    
    return ''.join(decrypted_text)

def encrypt(algorithm: str, text: str, key: str) -> str:
    algorithms = {
        'XOR': xor_encrypt,
        'AES': vigenere_encrypt,
        'DES': des_encrypt,
        'Caesar': caesar_encrypt,
        'Blowfish': blowfish_encrypt,
        'Twofish': twofish_encrypt,
        'Serpent': serpent_encrypt,
        'RSA': rsa_encrypt
    }
    if algorithm in algorithms:
        return algorithms[algorithm](text, key)
    else:
        raise ValueError(f"Алгоритм {algorithm} не реализован")

def decrypt(algorithm: str, encrypted_text: str, key: str) -> str:
    algorithms = {
        'XOR': xor_decrypt,
        'AES': vigenere_decrypt,
        'DES': des_decrypt,
        'Caesar': caesar_decrypt,
        'Blowfish': blowfish_decrypt,
        'Twofish': twofish_decrypt,
        'Serpent': serpent_decrypt,
        'RSA': rsa_decrypt
    }
    if algorithm in algorithms:
        return algorithms[algorithm](encrypted_text, key)
    else:
        raise ValueError(f"Алгоритм {algorithm} не реализован")

def encrypt_data(source_text: str, key_string: str) -> str:
    return xor_encrypt(source_text, key_string)

def decrypt_data(base64_text: str, key_string: str) -> str:
    return xor_decrypt(base64_text, key_string)
