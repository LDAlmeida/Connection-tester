#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import socket
import threading

class ConnectionTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Conexão")
        self.root.geometry("800x600")
        
        style = ttk.Style()
        style.configure("TLabel", foreground="white", background="#333")
        style.configure("TButton", foreground="white", background="#007bff")
        
        self.title_label = ttk.Label(root, text="Teste de Conexão", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=20)
        
        self.ip_entry = ttk.Entry(root)
        self.ip_entry.pack(pady=10)
        
        self.connect_button = ttk.Button(root, text="Conectar", command=self.connect)
        self.connect_button.pack(pady=5)
        
        self.status_label = ttk.Label(root, text="", font=("Helvetica", 16))
        self.status_label.pack(pady=5)
        
        self.server_socket = None
        self.client_socket = None
        self.connected = False
        
        threading.Thread(target=self.wait_for_connection).start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def set_status(self, status):
        self.status_label.config(text=status)
        if status == "Conectado":
            self.status_label.config(foreground="green")
        else:
            self.status_label.config(foreground="black")

    def connect(self):
        if self.connected:
            return
        
        ip = self.ip_entry.get()
        self.set_status("Conectando...")
        
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, 12345))
            self.connected = True
            self.set_status("Conectado")
        except:
            self.set_status("Falha na conexão")

    def wait_for_connection(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 12345))
        self.server_socket.listen(1)
        
        while True:
            client, address = self.server_socket.accept()
            self.client_socket = client
            self.connected = True
            self.set_status("Conectado")

    def on_close(self):
        self.root.destroy()

# Cria a janela principal
root = tk.Tk()
app = ConnectionTester(root)
root.mainloop()
