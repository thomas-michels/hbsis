import MySQLdb

#host: mysql.padawans.dev

class SquadDB():

    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans10', user='padawans10', passwd='wt2019')
    # ----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):

        comando_sql_select = "SELECT * FROM Squad as S LEFT JOIN SGBDS AS SG on S.id_sgbds = SG.id" \
                             " INNER JOIN LinguagensBackEnd AS LBE ON S.id_linguagem_back_end = LBE.id" \
                             " INNER JOIN FrameworkFrontEnd AS FFE ON S.id_framework_front_end = FFE.id;"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()

        return resultado

    def adicionar(self,nome, descricao, numero_pessoas, id_linguaguem_back_end, id_framework_front_end, id_sgbds):

        comando_sql_insert = f"INSERT INTO Squad " \
                             f"(nome, descricao, numero_pessoas, id_linguagem_back_end, id_framework_front_end, id_sgbds) " \
                             f"VALUES ('{nome}', '{descricao}', {numero_pessoas}, {id_linguaguem_back_end}, {id_framework_front_end}, {id_sgbds})"
        self.cursor.execute((comando_sql_insert))
        self.conexao.commit()

    def buscar(self, id):

        comando_sql_select = f"SELECT * FROM Squad WHERE id= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def alterar(self, id, nome, descricao, numero_pessoas, id_linguaguem_back_end, id_framework_front_end, id_sgbds):
        comando_alterar = f"update Squad SET nome = '{nome}', descricao = '{descricao}', numero_pessoas = {numero_pessoas}, id_linguagem_back_end = {int(id_linguaguem_back_end)}, id_framework_front_end = {int(id_framework_front_end)}, id_sgbds = {int(id_sgbds)} where id = {int(id)}"
        self.cursor.execute(comando_alterar)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM Squad WHERE id= {id}"
        self.cursor.execute(comando_sql_delete)
        self.conexao.commit()

if __name__ == '__main__':
    s_db = SquadDB()
    print(s_db.listar_todos())