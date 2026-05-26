from test import encrypt_data, decrypt_data

def main():
    user_text = input("Введите текст для шифрования (кириллица поддерживается): ")
    secret_key = input("Введите секретный ключ (пароль): ")
    if not user_text or not secret_key:
        print("Ошибка: Текст и ключ не могут быть пустыми!")
        return
    encrypted_result = encrypt_data(user_text, secret_key)
    print(encrypted_result)
    
    input_cipher = input("Вставьте зашифрованные данные (Base64): ")
    input_key = input("Введите секретный ключ для расшифровки: ")
    try:
        decrypted_result = decrypt_data(input_cipher, input_key)
        print(f"\nУСПЕШНО РАСШИФРОВАНО: {decrypted_result}")
    except Exception as e:
        print(f"\nОШИБКА ДЕШИФРОВАНИЯ: Неверный ключ или поврежденные данные! ({e})")

if __name__ == "__main__":
    main()
