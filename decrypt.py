#!/usr/bin/python3

#Formatfile : abc:sha256$BMLBVx5WUeKc1nHB$7aa12b7946468d198b5bf273b7ff924a2381707a5f7373af73efd68878cd91f7

import argparse
from werkzeug.security import check_password_hash
import signal
import sys

# (Ctrl+C)
def signal_handler(sig, frame):
    print('\n Saliendo...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def user_hash(wordlist_path, hashes_path):
    try:
        with open(hashes_path, "r") as hashes:
            for hash_line in hashes:
                hash_line = hash_line.strip()
                if ':' not in hash_line:
                    continue
                user, hash_value = hash_line.split(":", 1)

                try:
                    with open(wordlist_path, "r", errors="ignore") as file:
                        for line in file:
                            password = line.strip()
                            if check_password_hash(hash_value, password):
                                print(f"Contraseña encontrada para {user}: {password}")
                                break
                        else:
                            print(f"Contraseña no encontrada para {user} en el diccionario")
                except FileNotFoundError:
                    print(f"No se encontró el archivo de wordlist en la ruta: {wordlist_path}")
                    return
    except FileNotFoundError:
        print(f"No se encontró el archivo de hashes en la ruta: {hashes_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script para verificar contraseñas con hashes y una wordlist.")
    parser.add_argument('-w', '--wordlist', required=True, help="Ruta al archivo de wordlist")
    parser.add_argument('-H', '--hashes', required=True, help="Ruta al archivo de hashes")

    args = parser.parse_args()
    user_hash(args.wordlist, args.hashes)


