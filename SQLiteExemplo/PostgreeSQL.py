import psycopg2

def main():
    conn = psycopg2.connect("dbname=GeekWay user=postgres password=ifpbinfo")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_usuario;
    """)

    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print("%s - NOME: %s, E-MAIL: %s, SENHA: %s, DATA NASCIMENTO:
%s, PROFISSAO: %s, GENERO: %s, CIDADE: %s, ESTADO: %s, PAÍS: %s" %
              (usuario[0], usuario[1], usuario[2], usuario[3],
usuario[4], usuario[5], usuario[6], usuario[7], usuario[8],
usuario[9]))

    conn.close()

if __name__ == '__main__':
    main()
