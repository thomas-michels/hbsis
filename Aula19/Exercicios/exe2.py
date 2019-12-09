# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#

def separar_pessoas(cab, pess):
        pessoas = []

        for i in range(0, len(pess)):
                if int(pess[3][i]) >= 18:
                        pessoa = {"nome": pess[0][i], "telefone": pess[1][i], "email": pess[2][i], "idade": pess[3][i]}
                        pessoas.append(pessoa)

        return pessoas

pessoas = separar_pessoas(cab, pess)

#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#

for pessoa in pessoas:
        nome = pessoa["nome"]
        telefone = pessoa["telefone"]
        email = pessoa["email"]
        idade = pessoa["idade"]
        print(nome + " - " + telefone + " - " + email + " - " + idade)

#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)

for pessoa in pessoas:
        print(f'{pessoa["nome"]} - {pessoa["telefone"]} - {pessoa["email"]} - {pessoa["idade"]}')