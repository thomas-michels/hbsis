# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com
def ler(lista):
    lista_nomes = lista[1]
    tel = lista[3]
    email = lista[5]
    idade = lista[7]

    for i in range(1, len(lista_nomes)):
        print(f'{lista[0]}: {lista_nomes[i]} - {lista[2]}: {tel[i]}')
        print(f'{lista[6]} de {lista_nomes[i]} é {idade[i]}')
        print(f'{lista[4]} de {lista_nomes[i]} é {email[i]}\n')

# 2 - usando o for, imprima todos nomes um abaixo do outro



# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)