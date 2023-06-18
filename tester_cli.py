#!/usr/bin/env python3

import os
import socket
import platform
import threading

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    ip = socket.gethostbyname(socket.gethostname())
    system = platform.system()
    release = platform.release()
    print("==== Teste de Conexão ====")
    print(f"IP da Máquina: {ip}")
    print(f"Sistema Operacional: {system}")
    print(f"Versão do Sistema: {release}\n")

def display_menu():
    print("Selecione uma opção:")
    print("1. Conectar")
    print("2. Sair\n")

def connect():
    ip = input("Insira o endereço IP da máquina remota: ")
    print("Conectando...")
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, 12345))
        print("Conectado!")
        client_socket.close()
    except:
        print("Falha na conexão.")

def wait_for_connection():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    
    while True:
        client, address = server_socket.accept()
        print(f"Uma máquina se conectou! Endereço IP: {address[0]}")

def main():
    clear_screen()
    display_header()

    threading.Thread(target=wait_for_connection).start()

    while True:
        display_menu()
        choice = input("Opção: ")
        
        if choice == "1":
            clear_screen()
            display_header()
            connect()
            input("\nPressione Enter para continuar...")
            clear_screen()
            display_header()
        elif choice == "2":
            clear_screen()
            break
        else:
            clear_screen()
            display_header()
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()