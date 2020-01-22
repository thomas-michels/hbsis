import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula37')
from Controller.squad_controller import SquadController

squad = SquadController()
b = squad.alterar(3, "aninha", 'ss', 19, 'C++', "hoho")
print(b)
a = squad.listar_todos()
for i in a:
    print(i)

