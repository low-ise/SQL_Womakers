import sqlite3
import random as rd

conexao = sqlite3.connect('banco-exercicio-sql')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')


# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

## Cria lista de registros para inserção:
lista_alunas = [
    (1, "Ana", 20, "Psicologia"),
    (2, "Carina", 32, "Química"),
    (3, "Maria", 26, "Artes Visuais"),
    (4, "Helena", 17, "Matemática"),
    (5, "Jennifer", 18, "Direito"),
    (6, "Melissa", 23, "Engenharia"),
    (7, "Sônia", 28, "Engenharia"),
    (8, "Alessandra", 31, "Engenharia"),
    (9, "Gabriela", 19, "Engenharia"),
    (10, "Teresa", 18, "Engenharia"),
    ]

## Insere os registros e fecha a conexão:
try:
    cursor.executemany('INSERT INTO alunos(id, nome, idade, curso) VALUES (?, ?, ?, ?);', lista_alunas)
    conexao.commit()
except sqlite3.Error as e:
    print("Não foi possível inserir os registros:", e)
finally:
    conexao.close()


# 3. Consultas Básicas: Escreva consultas SQL para realizar as seguintes tarefas:
## Letra a)
a = "Selecionar todos os registros da tabela \"alunos\""
todos_registros = 'SELECT * FROM alunos;'

## Letra b)
b = "Selecionar o nome e a idade dos alunos com mais de 20 anos"
nome_idade_mais_20 = 'SELECT nome, idade FROM alunos WHERE idade>20;'

## Letra c)
c = "Selecionar os alunos do curso de \"Engenharia\" em ordem alfabética"
alunas_engenharia = 'SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome;'

## Letra d
d = "Contar o número total de alunos na tabela"
total_alunas = 'SELECT COUNT(id) FROM alunos;'

# Lista de queries
queries = [todos_registros,
           nome_idade_mais_20,
           alunas_engenharia,
           total_alunas]

letra_selecao = [a, b, c, d]
try:
    for selecao in range(len(queries)):
        query = queries[selecao]
        dados_query = cursor.execute(query)

        print("\n",letra_selecao[selecao])

        for aluno in dados_query:
            print(aluno)

        conexao.commit()
except sqlite3.Error as e:
    print("Não foi possível concluir a requisição:", e)
finally:
    conexao.close()


# 4. Atualização e Remoção
## Letra a)

a = "Atualize a idade de um aluno específico na tabela:\nAtualiza a idade do registo com id = 1 para 19 anos"
atualiza_idade = 'UPDATE alunos SET idade=19 WHERE nome=(SELECT nome FROM alunos WHERE id=1);'

## Letra b)

b = "Remova um aluno pelo seu ID:\nRemove o registro com id = 10"
remove_aluno = 'DELETE FROM alunos WHERE id=10;'

## Exibe resultado:
c = "Resultado:"

letra_selecao = [a, b, c]

queries = [atualiza_idade,
           remove_aluno,
           'SELECT * FROM alunos']

try:
    for selecao in range(len(queries)):
        query = queries[selecao]
        dados_query = cursor.execute(query)
        print("\n>",letra_selecao[selecao])

        for aluno in dados_query:
            print(aluno)

        conexao.commit()

except sqlite3.Error as e:
    print("Não foi possível concluir a requisição:", e)
finally:
    conexao.close()


# 5. Criar uma Tabela e Inserir Dados: Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cria_tabela = 'CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome VARCHAR(100) NOT NULL, idade INT, saldo FLOAT(10,4) NOT NULL);'

lista_clientes = [
    ("Chris", 42, 8540.546),
    ("Sandra", 65, 9468.21),
    ("Mariana", 25, 5248.452),
    ("Carolina", 50, 12654.854),
    ("Beatriz", 40, 508.360),
    ("Luiza", 35, 899.415),
    ("Débora", 39, 2224.4089),
    ("Nayara", 46, 5008.1543),
    ("Catarina", 53, 652.1547),
    ("Joana", 28, 992.4568),
    ]

## Cria a tabela, insere os registros e fecha a conexão:
try:
    cursor.execute(cria_tabela)
    cursor.executemany('INSERT INTO clientes(nome, idade, saldo) VALUES (?, ?, ?);', lista_clientes)
    conexao.commit()
except sqlite3.Error as e:
    print("Não foi possível inserir os registros:", e)
finally:
    conexao.close()


# 6. Consultas e Funções Agregadas: Escreva consultas SQL para realizar as seguintes tarefas:
## Letra a)
a = "Selecione o nome e a idade dos clientes com idade superior a 30 anos"
nome_idade_mais_30 = 'SELECT nome, idade FROM clientes WHERE idade>30;'

## Letra b)
b = "Calcule o saldo médio dos clientes"
saldo_medio = 'SELECT AVG(saldo) FROM clientes;'

## Letra c)
c = "Encontre o cliente com o saldo máximo"
cliente_saldo_max = 'SELECT * FROM clientes WHERE saldo=(SELECT MAX(saldo) FROM clientes);'

## Letra d)
d = "Conte quantos clientes têm saldo acima de 1000"
clientes_saldo_mais_1000 = 'SELECT COUNT(id) FROM clientes WHERE saldo>1000'

letra_selecao = [a, b, c, d]

queries = [nome_idade_mais_30,
           saldo_medio,
           cliente_saldo_max,
           clientes_saldo_mais_1000]

## Executa as queries e fecha a conexão
try:
    for selecao in range(len(queries)):
        query = queries[selecao]
        dados_query = cursor.execute(query)
        print("\n>",letra_selecao[selecao])

        for cliente in dados_query:
            print(cliente)

        conexao.commit()
except sqlite3.Error as e:
    print("Não foi possível concluir a requisição:", e)
finally:
    conexao.close()

# 7. Atualização e Remoção com Condições
## a) Atualize o saldo de um cliente específico.
## b) Remova um cliente pelo seu ID.



# 8. Junção de Tabelas: Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
# Insira algumas compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.