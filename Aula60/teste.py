
from Aula60.Model.Fortwo import Fortwo
from Aula60.Model.Base_local import BaseLocal
from Aula60.Model.Avião import Aviao
from Aula60.Model.Terminal import Terminal


def viagem(pessoa1, pessoa2, origem: BaseLocal, destino: BaseLocal):
    fortwo = Fortwo()

    if origem.saida(pessoa2):
        if origem.saida(pessoa1):
            if fortwo.set_motorista(pessoa1):
                if fortwo.set_passageiro(pessoa2):
                    fortwo.viagem(origem, destino)
                    if destino.entrada(pessoa1):
                        if destino.entrada(pessoa2):
                            pass

if __name__ == '__main__':
    viagem('piloto', 'oficial1', Terminal(), Aviao())
    viagem('piloto', '', Aviao(), Terminal())
    viagem('piloto', 'oficial2', Terminal(), Aviao())
    viagem('piloto', '', Aviao(), Terminal())
    #viagem('policial', 'presidiario', Terminal(), Aviao())
    #viagem('policial', '', Aviao(), Terminal())