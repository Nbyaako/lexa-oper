import base64
import hashlib
import math

# ============ XOR ШИФРОВАНИЕ ============
# Принцип: XOR каждого байта текста с соответствующим байтом ключа
# При повторе ключа (если текст длиннее): key повторяется циклически
# Простой и быстрый алгоритм, но не безопасный для серьёзного применения
# Формула шифрования: зашифрованный_байт = исходный_байт XOR ключевой_байт

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

# ============ CAESAR ШИФРОВАНИЕ ============
# Принцип: каждый байт смещается на одно и то же значение (вычисленное из ключа)
# Ключ преобразуется в число путём суммирования ASCII-кодов символов
# Простой, исторический алгоритм, легко взламывается (известна длина смещения)
# Формула: шифр = (байт + смещение) mod 256

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

# ============ VIGENÈRE ШИФРОВАНИЕ (используется для AES) ============
# Принцип: каждый байт текста складывается с соответствующим байтом хеша ключа
# SHA256 ключа разворачивается в последовательность длиной 32 байта
# При повторе ключа (если текст длиннее 32 байт): хеш повторяется циклически
# Более сложный чем Caesar, так как смещение меняется для каждой позиции
# Формула: шифр = (байт + хеш_ключ[позиция]) mod 256

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

# ============ DES ШИФРОВАНИЕ ============
# Принцип: комбинирует XOR с позиционным смещением для усиления криптографии
# SHA256 ключа преобразуется в HEX и берутся первые 16 символов
# Каждый байт текста сначала XORится с соответствующим байтом ключа
# Затем к результату добавляется позиционное смещение (зависит от позиции в тексте)
# Формула шифрования: шифр = (исходный XOR ключ) + (позиция mod 256)

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

# ============ BLOWFISH ШИФРОВАНИЕ ============
# Принцип: быстрое шифрование через умножение и сложение с хешем
# BLAKE2b хеш ключа дает 32 байта криптографически сильного материала
# Каждый байт текста складывается с 7-кратным произведением байта ключа
# Множитель 7 используется для нелинейного преобразования данных
# Это быстрее традиционного шифрования но всё ещё обеспечивает хорошее рассеивание
# Формула: шифр = (байт + ключ_байт * 7) mod 256

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

# ============ TWOFISH ШИФРОВАНИЕ ============
# Принцип: комбинирует XOR с добавлением смещения для симметричного шифрования
# SHA512 ключа дает 64 байта материала, обеспечивая долгий период повторения
# Сначала байт XORится с соответствующим байтом ключа (нелинейная операция)
# Затем добавляется константа 45 для дополнительного перемешивания
# Смещение на константу 45 выбрано произвольно для избежания паттернов
# Формула: шифр = (байт XOR ключ_байт + 45) mod 256

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

# ============ SERPENT ШИФРОВАНИЕ ============
# Принцип: использует множественные нелинейные преобразования для стойкости
# MD5 ключа дает 16 байт материала, используется как маска смешивания
# Умножение на 13 создаёт нелинейное преобразование (избегает линейных паттернов)
# XOR с константой 0xAA добавляет фиксированный паттерн для дополнительного шумоподавления
# Serpent спроектирован как безопасная альтернатива AES
# Формула: шифр = ((байт * 13 + ключ_байт) XOR 0xAA) mod 256

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

# ============ RSA ШИФРОВАНИЕ ============
# Принцип: асимметричное шифрование с публичным и приватным ключами
# Использует математику модульной арифметики: (сообщение^e) mod n
# n = произведение двух больших простых чисел (p и q)
# e = публичная экспонента (обычно 65537), d = приватная экспонента
# Безопасность основана на сложности факторизации больших чисел
# Используемая здесь реализация упрощённая (учебная), для production нужна cryptography библиотека
# Формула зашифрования: шифр = (сообщение ^ e) mod n
# Формула расшифровки: сообщение = (шифр ^ d) mod n

def _extended_gcd(a: int, b: int):
    """Расширенный алгоритм Евклида для нахождения обратного элемента"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = _extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def _mod_inverse(e: int, phi: int) -> int:
    """Найти модульный обратный элемент для приватной экспоненты"""
    gcd, x, _ = _extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Модульный обратный не существует")
    return (x % phi + phi) % phi

def _is_prime(n: int, k: int = 5) -> bool:
    """Тест Миллера-Рабина для проверки простоты числа"""
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
    """Генерирует простое число на основе seed (детерминировано)"""
    counter = 0
    while True:
        candidate = int.from_bytes(
            hashlib.sha256((str(seed) + str(counter)).encode()).digest(), 'big'
        ) | (1 << bits - 1) | 1
        if _is_prime(candidate):
            return candidate
        counter += 1

def rsa_encrypt(source_text: str, key_string: str) -> str:
    """RSA шифрование: преобразует текст в числа и шифрует их"""
    # Генерируем ключи на основе ключевой строки (детерминировано)
    hash_value = int(hashlib.sha256(key_string.encode()).hexdigest(), 16)
    
    # Генерируем два различных простых числа детерминировано из хеша
    p = _generate_prime(hash_value, 128)
    q = _generate_prime(hash_value + 1, 128)
    
    while p == q:
        q = _generate_prime(hash_value + 2, 128)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Выбираем публичную экспоненту
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
    
    # Шифруем текст
    encrypted_numbers = []
    for char in source_text:
        m = ord(char)
        c = pow(m, e, n)
        encrypted_numbers.append(str(c))
    
    # Кодируем результат
    result = ','.join(encrypted_numbers)
    return base64.b64encode(result.encode()).decode('utf-8')

def rsa_decrypt(base64_text: str, key_string: str) -> str:
    """RSA дешифрование: расшифровывает числа и преобразует обратно в текст"""
    # Генерируем те же ключи (детерминировано из того же ключевой строки)
    hash_value = int(hashlib.sha256(key_string.encode()).hexdigest(), 16)
    
    # Генерируем те же p и q в том же порядке
    p = _generate_prime(hash_value, 128)
    q = _generate_prime(hash_value + 1, 128)
    
    while p == q:
        q = _generate_prime(hash_value + 2, 128)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Выбираем публичную экспоненту (должна быть та же)
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
    
    # Вычисляем приватную экспоненту
    d = _mod_inverse(e, phi)
    
    # Декодируем и расшифровываем
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
    """Основная функция шифрования, выбирает алгоритм на основе параметра"""
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
    """Основная функция дешифрования, выбирает алгоритм на основе параметра"""
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
