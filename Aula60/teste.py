
from Aula60.Model.Pessoa import Pessoa
from Aula60.Model.Fortwo import Fortwo
from Aula60.Model.Avião import Aviao

p1 = Pessoa(1, 'aa')
p2 = Pessoa(2, 'bb')

av = Aviao()
fort = Fortwo(p1, p2)
print(fort.posicao_atual)
av.adicionar_pessoa(p1)
print(av.get_pessoas())
av.remover_pessoa(p1)
print(av.get_pessoas())
