import sys
sys.path.insert(0, 'c:\\Users\\milev\\Documents\\GitHub\\lexa-oper\\main')

import cryptolib

# Тест RSA
key = 'test_key_123'
plaintext = 'Hello RSA!'

# Шифруем
encrypted = cryptolib.encrypt('RSA', plaintext, key)
print(f'Исходный текст:  {plaintext}')
print(f'Зашифрованный:   {encrypted}')

# Дешифруем
decrypted = cryptolib.decrypt('RSA', encrypted, key)
print(f'Дешифрованный:   {decrypted}')

# Проверяем совпадение
if plaintext == decrypted:
    print('✓ RSA успешно работает!')
else:
    print('✗ Дешифрование не совпадает!')
