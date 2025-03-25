import sqlite3

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('estoque.db')
c = conn.cursor()

# Criar a tabela de produtos
c.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
