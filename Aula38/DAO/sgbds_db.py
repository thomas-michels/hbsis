import MySQLdb

#host: mysql.padawans.dev

class SgbdsDB():

    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans10', user='padawans10', passwd='wt2019')
    # ----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):

        comando_sql_select = "SELECT * FROM SGBDS"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()

        return resultado

    def adicionar(self,nome):

        comando_sql_insert = f"INSERT INTO SGBDS (nome) values ('{nome}')"
        self.cursor.execute((comando_sql_insert))
        self.conexao.commit()

    def buscar(self, id):

        comando_sql_select = f"SELECT * FROM SGBDS WHERE id= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def alterar(self, id, nome):
        comando_alterar = f"UPDATE SGBDS SET nome = '{nome}' where id = {id}"
        self.cursor.execute(comando_alterar)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM SGBDS WHERE id= {id}"
        self.cursor.execute(comando_sql_delete)
        self.conexao.commit()
