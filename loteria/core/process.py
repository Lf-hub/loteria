from .models import Jogo, NumeroSorteado, NumeroRepetido

class Base():
    def __init__(self, operation):
        self.operation = operation

    def get_repetidos(self):
        teste = NumeroSorteado.objects.all()
        print(teste)
        pass