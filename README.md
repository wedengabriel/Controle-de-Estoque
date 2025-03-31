# Controle de Estoque - Projeto de Lógica de Programação Aplicada 📦

## Descrição 📝

Este projeto é uma aplicação desenvolvida para gerenciar o controle de estoque de materiais em um almoxarifado, permitindo a adição, remoção e consulta de materiais. Ele foi desenvolvido como parte do trabalho acadêmico da disciplina de **Lógica de Programação Aplicada** no curso de **Análise e Desenvolvimento de Sistemas (ADS)** da **Universidade Internacional de Educação a Distância (Uninter)**. 🎓

## Funcionalidades ⚙️

- **Adicionar materiais**: Permite registrar novos materiais no banco de dados, especificando nome, categoria, fornecedor, quantidade, preço e data de entrada. ➕
- **Remover materiais**: Permite dar saída de materiais do estoque, ajustando a quantidade disponível no banco de dados. ➖
- **Atualizar quantidade de materiais**: Permite aumentar a quantidade de materiais disponíveis no estoque. 🔄
- **Filtro de pesquisa**: Oferece a funcionalidade de filtrar materiais por nome, categoria ou fornecedor para facilitar a busca. 🔍
- **Exibição de materiais**: Exibe todos os materiais cadastrados com informações como nome, categoria, fornecedor, quantidade, preço e data de entrada. 📊

## Tecnologias Utilizadas 💻

- **Python**: Linguagem de programação utilizada para desenvolvimento da aplicação. 🐍
- **Tkinter**: Biblioteca GUI utilizada para construir a interface gráfica. 🎨
- **SQLite**: Banco de dados relacional utilizado para armazenar as informações dos materiais. 📚

## Estrutura do Banco de Dados 🗄️

A aplicação utiliza um banco de dados SQLite chamado `almoxarifado.db`, que contém a tabela `materiais`. Esta tabela armazena as seguintes informações:

- **id** (INTEGER): Identificador único do material. 🔑
- **nome** (TEXT): Nome do material. 📦
- **categoria** (TEXT): Categoria do material. 📂
- **fornecedor** (TEXT): Nome do fornecedor do material. 🏢
- **quantidade** (INTEGER): Quantidade disponível do material no estoque. 🔢
- **preco** (REAL): Preço unitário do material. 💲
- **data_entrada** (TEXT): Data em que o material foi registrado no estoque. 📅

## Como Rodar o Projeto 🚀

1. **Instalar as dependências**: Certifique-se de ter o Python instalado em sua máquina. Caso não tenha, baixe e instale a versão mais recente do Python no [site oficial](https://www.python.org/downloads/). 🌍

2. **Banco de Dados SQLite**: O banco de dados será criado automaticamente quando o programa for executado pela primeira vez. 💾

3. **Rodando o código**:
   - Faça o download ou clone este repositório.
   - Navegue até o diretório do projeto e execute o arquivo Python:
     ```bash
     python controle_estoque.py
     ```

## Repositório no GitHub 🔗

Acesse o repositório do projeto no GitHub para obter mais detalhes, fazer contribuições ou relatar problemas: [Controle de Estoque - GitHub](https://github.com/wedengabriel/Controle-de-Estoque) 📍

## Autores 👨‍💻

- **Weden Gabriel da Silva Gomes**  
  Matrícula: 4170826  
  Curso: Análise e Desenvolvimento de Sistema (ADS) - Uninter 🎓