# Encapsulamento - esconder dsa outras classses
# Coloca um _ antes do atributo (CONVENÇÃO)

class Conta():
    def __init__(self, saldo):
        self._saldo = saldo
    def get_saldo(self):
        return self._saldo
    def set_saldo(self, numero):
        self._saldo = numero

conta1 = Conta(200.0)
conta2 = Conta(300.0)

print(conta1.get_saldo())