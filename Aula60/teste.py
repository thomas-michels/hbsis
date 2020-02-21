
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
                    if destino.entrada(pessoa1):
                        if destino.entrada(pessoa2):
                            fortwo.viagem(origem, destino)
                        else:
                            print("Erro 6")
                    else:
                        print("Erro 5")
                else:
                    print("Erro 4")
            else:
                print("Erro 3")
        else:
            print("Erro 2")
    else:
        print("Erro 1")


if __name__ == '__main__':

    terminal = Terminal()
    aviao = Aviao()

    viagem('piloto', 'oficial1', terminal, aviao)
    viagem('piloto', '', aviao, terminal)
    viagem('piloto', 'oficial2', terminal, aviao)
    viagem('piloto', '', aviao, terminal)
    viagem('piloto', 'chefe de servico', terminal, aviao)
    viagem('chefe de servico', '', aviao, terminal)
    viagem('chefe de servico', 'comissario1', terminal, aviao)
    viagem('chefe de servico', '', aviao, terminal)
    viagem('chefe de servico', 'comissario2', terminal, aviao)
    viagem('piloto', '', aviao, terminal)
    viagem('policial', 'presidiario', terminal, aviao)
    viagem('chefe de servico', '', aviao, terminal)
    viagem('chefe de servico', 'piloto', terminal, aviao)
