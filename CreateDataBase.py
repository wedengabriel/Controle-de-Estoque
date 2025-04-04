import sqlite3

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('almoxarifado.db')
c = conn.cursor()

# Criar a tabela de materiais (almoxarifado)
c.execute('''
    CREATE TABLE IF NOT EXISTS materiais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        fornecedor TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        data_entrada TEXT NOT NULL
    )
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
