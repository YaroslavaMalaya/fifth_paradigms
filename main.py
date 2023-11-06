def encrypt(text, key):
    result = []

    for ch in text:
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


def console():
    while True:
        command = input("\nEnter 'encrypt' to encrypt a file, 'decrypt' to decrypt a file or 'exit' to quit: ").strip().lower()

        if command == 'exit':
            print("Exiting the program.")
            break

        key = int(input("Enter encryption/decryption number-key: "))
        readFile = input("Enter the name of the input file: ").strip()
        writeFile = input("Enter the name of the output file: ").strip()
        text = readFromFile(readFile)

        if command == 'encrypt':
            result = encrypt(text, key)
        elif command == 'decrypt':
            result = decrypt(text, key)

        writeToFile(writeFile, result)
        print(f"The text has been successfully {command}ed and added in {writeFile}.")


if __name__ == '__main__':
    console()
