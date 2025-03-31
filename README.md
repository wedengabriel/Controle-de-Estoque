# Controle de Estoque - Projeto de Lógica de Programação Aplicada 🎆

## Descrição 📝

Este projeto é uma aplicação para gerenciar o controle de estoque de materiais em um almoxarifado, permitindo a adição, remoção e consulta de materiais. O projeto foi desenvolvido como parte do trabalho acadêmico da disciplina de **Lógica de Programação Aplicada** no curso de **Análise e Desenvolvimento de Sistemas (ADS)** do **Centro Universitário Internacional (Uninter)**. 🎓

## Funcionalidades ⚙️

- **Adicionar materiais**: Permite registrar novos materiais no banco de dados ou atualizar a quantidade de um material já existente. ➕
- **Remover materiais**: Permite dar saída de materiais do estoque, ajustando a quantidade disponível. ➖
- **Atualizar quantidade**: Possibilita a adição de novas unidades a um material já cadastrado. 🔄
- **Filtro de pesquisa**: Permite filtrar materiais por nome, categoria ou fornecedor para facilitar a busca. 🔍
- **Exibição de materiais**: Lista todos os materiais cadastrados com informações detalhadas. 📊

## Tecnologias Utilizadas 💻

- **Python**: Linguagem de programação principal do projeto. 🐍
- **Tkinter**: Biblioteca para criação da interface gráfica. 🎨
- **SQLite**: Banco de dados utilizado para armazenar os materiais. 📚

## Estrutura do Banco de Dados 🛂

A aplicação utiliza um banco de dados SQLite chamado `almoxarifado.db`, contendo a tabela `materiais`, com os seguintes campos:

- **id** (INTEGER): Identificador único do material. 🔑
- **nome** (TEXT): Nome do material. 🛋️
- **categoria** (TEXT): Categoria do material. 🛃️
- **fornecedor** (TEXT): Nome do fornecedor. 🏢
- **quantidade** (INTEGER): Quantidade disponível no estoque. 📈
- **preco** (REAL): Preço unitário do material. 💲
- **data_entrada** (TEXT): Data de entrada do material. 📅

## Como Rodar o Projeto 🚀

1. **Instalar as dependências**: Certifique-se de ter o Python instalado. Caso contrário, baixe a versão mais recente do [site oficial](https://www.python.org/downloads/). 🌐

2. **Criar o banco de dados**: Execute o arquivo `CreateDataBase.py` para criar a estrutura inicial do banco de dados:
   ```bash
   python CreateDataBase.py
   ```

3. **Rodar a aplicação**:
   - Navegue até o diretório do projeto e execute:
     ```bash
     python main.py
     ```
   - Isso abrirá a interface gráfica para gestão do estoque. 🌟

4. **Executável (.exe)**:
   - Caso utilize a versão empacotada com `PyInstaller`, certifique-se de que o arquivo `almoxarifado.db` esteja na mesma pasta que o arquivo `.exe`, garantindo o correto funcionamento da aplicação.

## Repositório no GitHub 🔗

Acesse o repositório do projeto no GitHub para mais detalhes, contribuições ou relatórios de problemas: [Controle de Estoque - GitHub](https://github.com/wedengabriel/Controle-de-Estoque) 📌

## Autor 👨‍💻

- **Weden Gabriel da Silva Gomes**  
  Matrícula: 4170826  
  Curso: Análise e Desenvolvimento de Sistemas (ADS) - Uninter 🎓

