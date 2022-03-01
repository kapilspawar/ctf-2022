#!/usr/bin/env python
import argparse
import sys


def generate_key(string, keyword):
    keyword = list(keyword)
    if len(string) == len(keyword):
        return keyword
    else:
        for i in range(len(string) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return "".join(keyword)


def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
        x = ord(string[i])
        if ord('A') <= x <= ord('Z'):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
        encrypt_text.append(chr(x))
    return "".join(encrypt_text)


def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = ord(encrypt_text[i])
        if 65 <= x <= 90:
            x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)


def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='vigenere-cipher.py', usage='%(prog)s [options]', allow_abbrev=True)
    parser.add_argument('--message', type=str, help='Upper Case String to encrypt/decrypt', required=True)
    parser.add_argument('--keyword', type=str, help='Upper Case Key to encrypt/decrypt', required=True)
    parser.add_argument('--mode', type=str, help='Mode whether encrypt/decrypt', choices=['encrypt', 'decrypt'],
                        default='decrypt')
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        print('Unknown arguments provided')
        sys.exit(1)
    MESSAGE = args.__getattribute__('message').upper()
    KEYWORD = args.__getattribute__('keyword').upper()
    MODE = args.__getattribute__('mode')
    KEY = generate_key(MESSAGE, KEYWORD)
    print("message: ", MESSAGE)
    print("keyword: ", KEYWORD)
    print("mode: ", MODE)
    print("key: ", KEY)

    encrypted_message = encryption(MESSAGE, KEY)
    if MODE == 'encrypt':
        print("Encrypted text: ", encryption(MESSAGE, KEY))
    elif MODE == 'decrypt':
        print("Decrypted text: ", decryption(MESSAGE, KEY))

    main()
