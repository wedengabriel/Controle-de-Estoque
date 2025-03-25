import tkinter as tk
from tkinter import ttk
import sqlite3

# Função para listar materiais
def listar_materiais():
    conn = sqlite3.connect('almoxarifado.db')
    c = conn.cursor()
    c.execute('SELECT * FROM materiais')
    rows = c.fetchall()
    for row in rows:
        treeview.insert("", "end", values=row)
    conn.close()

# Função para adicionar material
def adicionar_material():
    nome = entry_nome.get()
    categoria = entry_categoria.get()
    fornecedor = entry_fornecedor.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()
    data_entrada = entry_data_entrada.get()
    
    conn = sqlite3.connect('almoxarifado.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO materiais (nome, categoria, fornecedor, quantidade, preco, data_entrada)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, categoria, fornecedor, quantidade, preco, data_entrada))
    conn.commit()
    conn.close()
    listar_materiais()  # Atualiza a lista de materiais

# Configuração da interface gráfica
root = tk.Tk()
root.title("Controle de Almoxarifado")

# Tornar a janela responsiva
root.geometry("800x600")  # Tamanho inicial
root.minsize(600, 400)  # Tamanho mínimo

# Configuração do layout com grid
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Campos de entrada
label_nome = tk.Label(frame, text="Nome do Material:")
label_nome.grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, sticky="ew", pady=5)

label_categoria = tk.Label(frame, text="Categoria:")
label_categoria.grid(row=1, column=0, sticky="w", pady=5)
entry_categoria = tk.Entry(frame)
entry_categoria.grid(row=1, column=1, sticky="ew", pady=5)

label_fornecedor = tk.Label(frame, text="Fornecedor:")
label_fornecedor.grid(row=2, column=0, sticky="w", pady=5)
entry_fornecedor = tk.Entry(frame)
entry_fornecedor.grid(row=2, column=1, sticky="ew", pady=5)

label_quantidade = tk.Label(frame, text="Quantidade:")
label_quantidade.grid(row=3, column=0, sticky="w", pady=5)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=3, column=1, sticky="ew", pady=5)

label_preco = tk.Label(frame, text="Preço (R$):")
label_preco.grid(row=4, column=0, sticky="w", pady=5)
entry_preco = tk.Entry(frame)
entry_preco.grid(row=4, column=1, sticky="ew", pady=5)

label_data_entrada = tk.Label(frame, text="Data de Entrada:")
label_data_entrada.grid(row=5, column=0, sticky="w", pady=5)
entry_data_entrada = tk.Entry(frame)
entry_data_entrada.grid(row=5, column=1, sticky="ew", pady=5)

# Botão para adicionar material
button_adicionar = tk.Button(frame, text="Adicionar Material", command=adicionar_material)
button_adicionar.grid(row=6, column=0, columnspan=2, pady=10)

# Treeview para listar os materiais
treeview_frame = tk.Frame(frame)
treeview_frame.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")

# Criando a árvore de visualização (Treeview)
treeview = ttk.Treeview(treeview_frame, columns=("ID", "Nome", "Categoria", "Fornecedor", "Quantidade", "Preço", "Data de Entrada"), show="headings")
treeview.heading("ID", text="ID")
treeview.heading("Nome", text="Nome")
treeview.heading("Categoria", text="Categoria")
treeview.heading("Fornecedor", text="Fornecedor")
treeview.heading("Quantidade", text="Quantidade")
treeview.heading("Preço", text="Preço")
treeview.heading("Data de Entrada", text="Data de Entrada")

# Definindo as colunas para redimensionamento automático
treeview.column("ID", width=50, anchor="center")
treeview.column("Nome", width=150, anchor="w")
treeview.column("Categoria", width=100, anchor="w")
treeview.column("Fornecedor", width=150, anchor="w")
treeview.column("Quantidade", width=100, anchor="center")
treeview.column("Preço", width=100, anchor="center")
treeview.column("Data de Entrada", width=150, anchor="w")

# Adicionar a treeview ao frame
treeview.pack(fill=tk.BOTH, expand=True)

# Listar materiais no início
listar_materiais()

# Tornar a janela responsiva
frame.grid_rowconfigure(7, weight=1)  # Permite que a Treeview expanda conforme o tamanho da janela
frame.grid_columnconfigure(1, weight=1)  # Permite que as colunas de entrada se expandam

root.mainloop()
