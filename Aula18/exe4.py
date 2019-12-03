#Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )
for i in range(1, len(cerveja)):
    print(f'{cerveja[0][0]}: {cerveja[i][0]} - {cerveja[0][1]}: {cerveja[i][1]} - {cerveja[0][2]}: {cerveja[i][2]} - {cerveja[0][3]}: {cerveja[i][3]}')

# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.

def receber_tupla(tupla):
    dic = {"marca": tupla[0], "tipo": tupla[1], "ibu": tupla[2], "preco": tupla[3]}
    return dic

tupla = cerveja[1]
print(receber_tupla(tupla))