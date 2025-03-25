import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk

# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()
    
    if not nome or not quantidade or not preco:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    # Conectar ao banco de dados
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    
    # Inserir o novo produto no banco de dados
    c.execute('''
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
    ''', (nome, int(quantidade), float(preco)))
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
    listar_produtos()

# Função para registrar a venda de um produto
def registrar_venda():
    produto_id = entry_produto_id.get()
    quantidade_venda = entry_quantidade_venda.get()
    
    if not produto_id or not quantidade_venda:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    # Conectar ao banco de dados
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    
    # Verificar a quantidade disponível
    c.execute('SELECT quantidade FROM produtos WHERE id = ?', (produto_id,))
    result = c.fetchone()
    
    if result is None:
        messagebox.showerror("Erro", "Produto não encontrado!")
        return
    
    quantidade_estoque = result[0]
    
    if quantidade_estoque < int(quantidade_venda):
        messagebox.showerror("Erro", "Quantidade insuficiente em estoque!")
        return
    
    # Atualizar a quantidade do produto
    c.execute('''
        UPDATE produtos
        SET quantidade = quantidade - ?
        WHERE id = ?
    ''', (int(quantidade_venda), produto_id))
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
    listar_produtos()

# Função para listar todos os produtos no estoque
def listar_produtos():
    # Limpar a lista existente
    for item in treeview.get_children():
        treeview.delete(item)
    
    # Conectar ao banco de dados
    conn = sqlite3.connect('estoque.db')
    c = conn.cursor()
    
    # Obter todos os produtos
    c.execute('SELECT * FROM produtos')
    produtos = c.fetchall()
    
    for produto in produtos:
        treeview.insert("", "end", values=(produto[0], produto[1], produto[2], produto[3]))
    
    conn.close()

# Criar a janela principal
root = tk.Tk()
root.title("Controle de Estoque")
root.geometry("600x400")  # Definindo um tamanho fixo para a janela
root.resizable(False, False)  # Impede o redimensionamento da janela

# Estilos
root.configure(bg="#f0f0f0")
font = ("Arial", 12)
label_font = ("Arial", 10, "bold")

# Campos para adicionar produto
tk.Label(root, text="Nome do Produto:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nome = tk.Entry(root, font=font, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Quantidade:", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_quantidade = tk.Entry(root, font=font, width=30)
entry_quantidade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Preço:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_preco = tk.Entry(root, font=font, width=30)
entry_preco.grid(row=2, column=1, padx=10, pady=5)

btn_adicionar = tk.Button(root, text="Adicionar Produto", font=font, command=adicionar_produto, width=20, bg="#4CAF50", fg="white")
btn_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

# Campos para registrar venda
tk.Label(root, text="ID do Produto:", font=label_font, bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_produto_id = tk.Entry(root, font=font, width=30)
entry_produto_id.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Quantidade Vendida:", font=label_font, bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_quantidade_venda = tk.Entry(root, font=font, width=30)
entry_quantidade_venda.grid(row=5, column=1, padx=10, pady=5)

btn_venda = tk.Button(root, text="Registrar Venda", font=font, command=registrar_venda, width=20, bg="#FF5722", fg="white")
btn_venda.grid(row=6, column=0, columnspan=2, pady=10)

# Árvore para exibir o estoque com barra de rolagem
frame_treeview = tk.Frame(root, bg="#f0f0f0")
frame_treeview.grid(row=7, column=0, columnspan=2, pady=10)

treeview = ttk.Treeview(frame_treeview, columns=("ID", "Nome", "Quantidade", "Preço"), show="headings", height=5)
treeview.grid(row=0, column=0)

treeview.heading("ID", text="ID")
treeview.heading("Nome", text="Nome")
treeview.heading("Quantidade", text="Quantidade")
treeview.heading("Preço", text="Preço")

# Adicionar barra de rolagem
scrollbar = ttk.Scrollbar(frame_treeview, orient="vertical", command=treeview.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

treeview.configure(yscrollcommand=scrollbar.set)

# Listar os produtos quando a aplicação iniciar
listar_produtos()

# Iniciar a interface gráfica
root.mainloop()
