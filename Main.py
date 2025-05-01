import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import os
import sys
import ctypes

# Função para listar materiais com filtro
def listar_materiais(filtro_nome='', filtro_categoria='', filtro_fornecedor=''):
    treeview.delete(*treeview.get_children())  # Limpa a lista antes de atualizar
    conn = sqlite3.connect('almoxarifado.db')
    c = conn.cursor()

    # Modifica a consulta para incluir filtros
    c.execute('''
        SELECT * FROM materiais
        WHERE nome LIKE ? AND categoria LIKE ? AND fornecedor LIKE ?
    ''', (f"%{filtro_nome}%", f"%{filtro_categoria}%", f"%{filtro_fornecedor}%"))
    
    rows = c.fetchall()
    for row in rows:
        treeview.insert("", "end", values=row)
    conn.close()

# Função para adicionar material ou atualizar quantidade existente
def adicionar_material():
    nome = entry_nome.get().strip()
    categoria = entry_categoria.get().strip()
    fornecedor = entry_fornecedor.get().strip()
    quantidade = entry_quantidade.get().strip()
    preco = entry_preco.get().strip()
    data_entrada = entry_data_entrada.get().strip()

    if not nome or not categoria or not fornecedor or not quantidade or not preco or not data_entrada:
        tk.messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return

    try:
        quantidade = int(quantidade)  # Garante que a quantidade seja um número inteiro
        preco = float(preco)  # Garante que o preço seja um número decimal
    except ValueError:
        tk.messagebox.showwarning("Aviso", "Quantidade deve ser um número inteiro e Preço um número decimal!")
        return

    conn = sqlite3.connect('almoxarifado.db')
    c = conn.cursor()

    # Verifica se o material já existe no banco de dados
    c.execute('''
        SELECT id, quantidade FROM materiais 
        WHERE nome = ? AND categoria = ? AND fornecedor = ?
    ''', (nome, categoria, fornecedor))
    
    resultado = c.fetchone()
    
    if resultado:
        # Se o material já existir, apenas atualiza a quantidade
        id_material, quantidade_atual = resultado
        nova_quantidade = quantidade_atual + quantidade
        c.execute('''
            UPDATE materiais SET quantidade = ? WHERE id = ?
        ''', (nova_quantidade, id_material))
    else:
        # Caso contrário, adiciona o material como novo
        c.execute('''
            INSERT INTO materiais (nome, categoria, fornecedor, quantidade, preco, data_entrada)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, categoria, fornecedor, quantidade, preco, data_entrada))

    conn.commit()
    conn.close()
    listar_materiais()  # Atualiza a lista de materiais

    # Limpar as caixas de texto após a operação
    entry_nome.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_fornecedor.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_data_entrada.delete(0, tk.END)

# Função para adicionar quantidade ao material existente
def adicionar_quantidade():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um item para adicionar quantidade.")
        return

    item = treeview.item(selected_item)
    material_id = item["values"][0]  # Obtendo o ID do material
    quantidade_atual = item["values"][4]  # Obtendo a quantidade atual
    
    try:
        quantidade_adicionar = int(entry_adicionar.get())  # Obtém a quantidade digitada
        if quantidade_adicionar <= 0:
            messagebox.showwarning("Aviso", "A quantidade adicionada deve ser maior que zero.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para a quantidade a ser adicionada.")
        return
    
    nova_quantidade = quantidade_atual + quantidade_adicionar
    
    # Atualiza o banco de dados
    conn = sqlite3.connect('almoxarifado.db')
    c = conn.cursor()
    c.execute('''
        UPDATE materiais 
        SET quantidade = ? 
        WHERE id = ?
    ''', (nova_quantidade, material_id))
    conn.commit()
    conn.close()
    
    listar_materiais()  # Atualiza a exibição

    # Limpar a caixa de texto após a operação
    entry_adicionar.delete(0, tk.END)

# Função para remover material (dar saída)
def remover_material():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um item para remover.")
        return

    item = treeview.item(selected_item)
    material_id = item["values"][0]  # Obtendo o ID do material
    quantidade_atual = item["values"][4]  # Obtendo a quantidade atual
    
    try:
        quantidade_remover = int(entry_saida.get())  # Obtém a quantidade digitada
        if quantidade_remover <= 0:
            messagebox.showwarning("Aviso", "A quantidade de saída deve ser maior que zero.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para a quantidade de saída.")
        return
    
    nova_quantidade = quantidade_atual - quantidade_remover
    if nova_quantidade < 0:
        messagebox.showerror("Erro", "Quantidade insuficiente para remoção.")
        return
    
    # Atualiza o banco de dados
    conn = sqlite3.connect('almoxarifado.db')
    c = conn.cursor()
    c.execute('''
        UPDATE materiais 
        SET quantidade = ? 
        WHERE id = ?
    ''', (nova_quantidade, material_id))
    conn.commit()
    conn.close()
    
    listar_materiais()  # Atualiza a exibição

    # Limpar a caixa de texto após a operação
    entry_saida.delete(0, tk.END)

# Função para filtrar materiais
def filtrar_materiais():
    filtro_nome = entry_filtro_nome.get().strip()
    filtro_categoria = entry_filtro_categoria.get().strip()
    filtro_fornecedor = entry_filtro_fornecedor.get().strip()
    listar_materiais(filtro_nome, filtro_categoria, filtro_fornecedor)

# Criação da interface
root = tk.Tk()
root.title("Controle de Estoque")

# Maximizar a janela ao iniciar
root.state('zoomed')

# Icone do app
CAMINHO_ICONE = os.path.join(os.path.dirname(__file__), 'dist', 'Icons', 'armazem-convertico.ico')
root.iconbitmap(CAMINHO_ICONE)

# Define o ícone da taskbar (Windows)
if sys.platform == "win32":
    app_id = 'meu.app.estoque'  # Pode ser qualquer identificador único
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

# Definir o tamanho do frame para ocupar toda a janela
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Treeview para mostrar os materiais
treeview = ttk.Treeview(frame, columns=("ID", "Nome", "Categoria", "Fornecedor", "Quantidade", "Preço", "Data de Entrada"), show="headings")
treeview.heading("ID", text="ID")
treeview.heading("Nome", text="Nome")
treeview.heading("Categoria", text="Categoria")
treeview.heading("Fornecedor", text="Fornecedor")
treeview.heading("Quantidade", text="Quantidade")
treeview.heading("Preço", text="Preço")
treeview.heading("Data de Entrada", text="Data de Entrada")
treeview.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Campos para adicionar materiais
label_nome = tk.Label(frame, text="Nome do Material:")
label_nome.grid(row=1, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=1, column=1, sticky="ew", pady=5)

label_categoria = tk.Label(frame, text="Categoria:")
label_categoria.grid(row=2, column=0, sticky="w", pady=5)
entry_categoria = tk.Entry(frame)
entry_categoria.grid(row=2, column=1, sticky="ew", pady=5)

label_fornecedor = tk.Label(frame, text="Fornecedor:")
label_fornecedor.grid(row=3, column=0, sticky="w", pady=5)
entry_fornecedor = tk.Entry(frame)
entry_fornecedor.grid(row=3, column=1, sticky="ew", pady=5)

label_quantidade = tk.Label(frame, text="Quantidade:")
label_quantidade.grid(row=4, column=0, sticky="w", pady=5)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=4, column=1, sticky="ew", pady=5)

label_preco = tk.Label(frame, text="Preço:")
label_preco.grid(row=5, column=0, sticky="w", pady=5)
entry_preco = tk.Entry(frame)
entry_preco.grid(row=5, column=1, sticky="ew", pady=5)

label_data_entrada = tk.Label(frame, text="Data de Entrada:")
label_data_entrada.grid(row=6, column=0, sticky="w", pady=5)
entry_data_entrada = tk.Entry(frame)
entry_data_entrada.grid(row=6, column=1, sticky="ew", pady=5)

# Botão para adicionar ou atualizar material
button_adicionar = tk.Button(frame, text="Adicionar/Atualizar Material", command=adicionar_material)
button_adicionar.grid(row=7, column=0, columnspan=2, pady=10)

# Filtro de pesquisa
label_filtro_nome = tk.Label(frame, text="Filtro Nome:")
label_filtro_nome.grid(row=8, column=0, sticky="w", pady=5)
entry_filtro_nome = tk.Entry(frame)
entry_filtro_nome.grid(row=8, column=1, sticky="ew", pady=5)

label_filtro_categoria = tk.Label(frame, text="Filtro Categoria:")
label_filtro_categoria.grid(row=9, column=0, sticky="w", pady=5)
entry_filtro_categoria = tk.Entry(frame)
entry_filtro_categoria.grid(row=9, column=1, sticky="ew", pady=5)

label_filtro_fornecedor = tk.Label(frame, text="Filtro Fornecedor:")
label_filtro_fornecedor.grid(row=10, column=0, sticky="w", pady=5)
entry_filtro_fornecedor = tk.Entry(frame)
entry_filtro_fornecedor.grid(row=10, column=1, sticky="ew", pady=5)

button_filtro = tk.Button(frame, text="Filtrar", command=filtrar_materiais)
button_filtro.grid(row=11, column=0, columnspan=2, pady=10)

# Campos para adicionar/remover quantidade
label_adicionar = tk.Label(frame, text="Quantidade a Adicionar:")
label_adicionar.grid(row=12, column=0, sticky="w", pady=5)
entry_adicionar = tk.Entry(frame)
entry_adicionar.grid(row=12, column=1, sticky="ew", pady=5)

button_adicionar_quantidade = tk.Button(frame, text="Adicionar Quantidade", command=adicionar_quantidade)
button_adicionar_quantidade.grid(row=13, column=0, columnspan=2, pady=10)

label_saida = tk.Label(frame, text="Quantidade a Remover:")
label_saida.grid(row=14, column=0, sticky="w", pady=5)
entry_saida = tk.Entry(frame)
entry_saida.grid(row=14, column=1, sticky="ew", pady=5)

button_remover = tk.Button(frame, text="Remover Material", command=remover_material)
button_remover.grid(row=15, column=0, columnspan=2, pady=10)

# Iniciar a aplicação
listar_materiais()
root.mainloop()