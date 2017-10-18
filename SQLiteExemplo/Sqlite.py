import sqlite3

conn = sqlite3.connect("redesocial.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE usuario(
    id INTEREGER,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE,
    genero VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha TEXT
)
""")

conn.close()

print("Tabela criada com sucesso! Volte sempre e fique sempre de olho em nossos serviços oferecidos! :D")
