# ----- Importar biblioteca do Mysql
import MySQLdb
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula34')
from model.pessoa import Pessoa

class PessoaDb:
    # ----- Configurar a conexão
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    # ----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):
        # ----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM 01_MDG_PESSOA AS P LEFT JOIN 01_MDG_ENDERECO AS E ON P.ENDERECO_ID = E.ID"
        self.cursor.execute(comando_sql_select)
        # ---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        # print(resultado) OK
        lista_pessoas_classe = self.converter_tabela_classe(resultado)
        return lista_pessoas_classe

    def adicionar(self,nome, sobrenome, idade, id_endereco):
        comando_sql_insert = f"INSERT INTO 01_MDG_PESSOA (NOME, SOBRENOME, IDADE, ENDERECO_ID) VALUES ('{nome}', '{sobrenome}', {idade}, {id_endereco})"
        self.cursor.execute((comando_sql_insert))
        self.conexao.commit()

    def buscar_por_id(self, id):
        # ----- Criação do comando SQL e passado para o cursor
        comando_sql_select = f"SELECT * FROM 01_MDG_PESSOA WHERE ID= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM 01_MDG_PESSOA WHERE ID= {id}"
        self.cursor.execute(comando_sql_delete)
        self.conexao.commit()

    def converter_tabela_classe(self, lista_tuplas):
        # cria uma lista para armazenar os dicionarios
        lista_pessoas = []

        for p in lista_tuplas:
            # ----- Criação do objeto da classe pessoa
            p1 = Pessoa()
            # --- pega cada posição da tupla e atribui a uma chave do dicionário
            p1.id = p[0]
            p1.nome = p[1]
            p1.sobrenome = p[2]
            p1.idade = p[3]
            p1.endereco.id = p[5]
            p1.endereco.logradouro = p[6]
            p1.endereco.numero = p[7]
            p1.endereco.complemento = p[8]
            p1.endereco.bairro = p[9]
            p1.endereco.cidade = p[10]
            p1.endereco.cep = p[11]
            lista_pessoas.append(p1)

        return lista_pessoas

if __name__ == '__main__':
    p = PessoaDb()
    a = p.listar_todos()
   # for i in a:
       # print(i.endereco)