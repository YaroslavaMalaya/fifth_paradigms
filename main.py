def encrypt(raw_text, key):
    result = []

    for ch in raw_text:
        if ch.isupper():
            result.append(chr((ord(ch) - 65 + key) % 26 + 65))
        elif ch.islower():
            result.append(chr((ord(ch) - 97 + key) % 26 + 97))
        else:
            result.append(ch)

    return ''.join(result)


def decrypt(encrypted_text, key):
    if key > 26:
        key = key % 26
    result = []

    for ch in encrypted_text:
        if ch.isupper():
            result.append(chr((ord(ch) - 65 - key + 26) % 26 + 65))
        elif ch.islower():
            result.append(chr((ord(ch) - 97 - key + 26) % 26 + 97))
        else:
            result.append(ch)

    return ''.join(result)


def readFromFile(path):
    with open(path, 'r') as file:
        return file.read()


def writeToFile(path, text):
    with open(path, 'w') as file:
        file.write(text)
