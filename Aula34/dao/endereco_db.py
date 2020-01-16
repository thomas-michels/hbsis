import MySQLdb
from model.endereco import Endereco


class EnderecoDb():
    # ----- Configurar a conexão
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    # ----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):
        # ----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM 01_MDG_ENDERECO"
        self.cursor.execute(comando_sql_select)
        # ---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        lista_pessoas_classe = self.converter_tabela_classe(resultado)
        return lista_pessoas_classe

    def buscar_por_id(self, id):
        # ----- Criação do comando SQL e passado para o cursor
        comando_sql_select = f"SELECT * FROM 01_MDG_ENDERECO WHERE ID= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        # cria uma lista para armazenar os dicionarios
        lista_enderecos = []
        for e in lista_tuplas:
            # ----- Criação do objeto da classe pessoa
            e1 = Endereco()
            # --- pega cada posição da tupla e atribui a uma chave do dicionário
            e1.id = e[0]
            e1.logradouro = e[1]
            e1.numero = e[2]
            e1.complemento = e[3]
            e1.bairro = e[4]
            e1.cidade = e[5]
            e1.cep = e[6]
            lista_enderecos.append(e1)
        return lista_enderecos