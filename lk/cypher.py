secret_key = "keykey"

#Алгоритм Виженера
def vigenere(text: str, key: str, encrypt=True):
    result = ""  # Создание переменной для хранения результата шифрования или дешифрования
    for i in range(len(text)):  # Итерация по каждому символу в тексте
        letter_n = ord(text[i])  # Получение числового значения текущего символа текста
        key_n = ord(key[i % len(key)])  # Получение числового значения символа ключа, который соответствует текущему символу текста
        if encrypt:  # Если флаг encrypt установлен в True, то выполняется шифрование
            value = (letter_n + key_n) % 1114112  # Вычисление нового числового значения символа после шифрования
        else:  # Если флаг encrypt установлен в False, то выполняется дешифрование
            value = (letter_n - key_n) % 1114112  # Вычисление нового числового значения символа после дешифрования
        result += chr(value)  # Преобразование числового значения обратно в символ и добавление его к результату
    return result  # Возвращение зашифрованного или расшифрованного текста

#Функиця Шифрования
def encrypt(text: str):
    return vigenere(text=text, key=secret_key, encrypt=True)

#Функция Дешифрования
def decrypt(text: str):
    return vigenere(text=text, key=secret_key, encrypt=False)
