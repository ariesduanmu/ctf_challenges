# -*- coding: utf-8 -*-
import tarfile
import os

import gnupg
import secrets

TAR_FILE = "encryptor.tar"
ENCRYPTED_FILE = "fuck_my_files.gpg"

def encrypt_files(src):
    with tarfile.open(TAR_FILE, "w:gz") as tar:
        tar.add(src)

    passphrase = secrets.token_hex(32)
    gpg = gnupg.GPG()
    with open(TAR_FILE, 'rb') as f:
        gpg.encrypt(f.read(),
                    recipients=None,
                    symmetric='AES256',
                    passphrase=passphrase,
                    armor=True,
                    output=ENCRYPTED_FILE)

    os.remove(TAR_FILE)
    return passphrase

def decrypt_files(passphrase):
    gpg = gnupg.GPG()
    with open(ENCRYPTED_FILE) as f:
        gpg.decrypt(f.read(),
                    passphrase=passphrase,
                    output=TAR_FILE)

if __name__ == '__main__':
    passphrase = encrypt_files(r"D:\test")
    decrypt_files(passphrase)
