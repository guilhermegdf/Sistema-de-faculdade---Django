from .pessoas import Pessoa

class Coordenador(Pessoa):

    class Meta:
        managed = False
        db_table = 'contas_coordenador'