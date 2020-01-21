import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula37')
from Controller.squad_controller import SquadController

squad = SquadController()
b = squad.buscar(2)
print(b)
a = squad.listar_todos()
for i in a:
    print(i)

