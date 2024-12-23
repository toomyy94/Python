import re

class Conta:
    numero_de_conta = 0

    def __init__(self, nome, nif):
        self.nome = nome
        self.nif = nif
        self.saldo = 0
        self.pin = None
        self.historico_de_operacoes = []
        Conta.numero_de_conta += 1
        self.numero_da_conta = Conta.numero_de_conta

    def definir_pin(self, pin):
        pinValido = True
        upper_count = 0
        lower_count = 0
        special_count = 0
        special_characters = ['$', '@', '#', '%', '!', '*']

        if not (6 <= len(pin) <= 8):
            print('Palavra passe precisa ter tamanho minimo de 6.' if len(pin) < 6 else 'Palavra passe nao pode ter tamanho superior a 8.')
            pinValido = False

        for char in pin:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            elif char in special_characters:
                special_count += 1

        if upper_count == 0:
            print('Palavra passe precisa conter uma letra maiuscula.')
            pinValido = False
        if lower_count == 0:
            print('Palavra passe precisa conter uma letra minuscula.')
            pinValido = False
        if special_count == 0:
            print("Palavra passe precisa conter pelo menos um caratere especial ['$', '@', '#', '%', '!', '*'] .")
            pinValido = False

        if pinValido:
            self.pin = pin

        return pinValido

    def acesso(self, pin):
        return self.pin == pin

    def depositar(self, valor):
        if self.pin is None:
            print("Palavra passe nao definida.")
            return False
        if valor <= 0:
            print("Deposito invalido.")
            return False
        self.saldo += valor
        self.historico_de_operacoes.append(f"Operacao numero:  {len(self.historico_de_operacoes) + 1} Valor:  {valor}")
        #print(f"Deposito de {valor} realizado com sucesso.")
        return True

    def levantar(self, valor):
        if self.pin is None:
            print("Palavra passe nao definida.")
            return False
        if valor <= 0:
            print("Levantamento invalido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente em conta.")
            return False
        self.saldo -= valor
        self.historico_de_operacoes.append(f"Operacao numero:  {len(self.historico_de_operacoes) + 1} Valor:  -{valor}")
        #print(f"Levantamento de {valor} realizado com sucesso.")
        return True

    def consulta(self):
        return self.saldo

    def historico(self):
        for operacao in self.historico_de_operacoes:
            print(operacao)
        print(f"Saldo atual:  {self.saldo}")

class EBank:
    def __init__(self, nome):
        self.nome = nome
        self._contas = {} #dicionário
        self.transacoes_pendentes = [] #lista

    def abrir_conta(self, nome, NIF):
        conta = Conta(nome, NIF)
        self._contas[conta.numero_da_conta] = conta
        return conta

    def aceder_conta(self, numero_da_conta, pin):
        conta = self._contas.get(numero_da_conta)
        if conta.pin is None:
            print("Palavra passe nao definida.")
            return None
        if conta.pin != pin:
            print("Palavra passe invalida.")
            return None
        if conta.numero_da_conta != numero_da_conta:
            print("Numero de conta invalido.")
            return None
        if len(pin) < 6:
            print("Palavra passe precisa ter tamanho minimo de 6.")
            return None
        return conta

    def encerrar_conta(self, numero_da_conta, pin):
        conta = self._contas.get(numero_da_conta)
        if conta is None:
            print("Numero de conta invalido.")
            return False
        if conta.pin is None:
            print("Palavra passe nao definida.")
            return False
        if conta.pin != pin:
            print("Palavra passe invalida.")
            return False
        if len(pin) < 6:
            print("Palavra passe precisa ter tamanho minimo de 6.")
            return False
        del self._contas[numero_da_conta]
        #print(f"Conta {numero_da_conta} encerrada com sucesso.")
        return True

    def numero_de_contas_ativas(self):
        return len(self._contas)


    def transferencia(self, num_conta_origem, num_conta_destino, valor, instantanea=True):
        conta_origem = self._contas.get(num_conta_origem)
        conta_destino = self._contas.get(num_conta_destino)
        if conta_origem is None or conta_destino is None or valor <= 0:
            print("Transferencia invalida.")
            return False
        if instantanea:
            if conta_origem.saldo < valor:
                print("Saldo insuficiente em conta.")
                return False
            conta_origem.saldo -= valor
            conta_destino.saldo += valor
            conta_origem.historico_de_operacoes.append(f"Operacao numero:  {len(conta_origem.historico_de_operacoes) + 1} Valor:  -{valor}")
            conta_destino.historico_de_operacoes.append(f"Operacao numero:  {len(conta_destino.historico_de_operacoes) + 1} Valor:  {valor}")
            #print(f"Transferência de {valor} de conta {num_conta_origem} para conta {num_conta_destino} realizada com sucesso.")
        else:
            self.transacoes_pendentes.append((num_conta_origem, num_conta_destino, valor))
            #print(f"Transferência de {valor} de conta {num_conta_origem} para conta {num_conta_destino} agendada.")
        return True

    def processamento(self):
        for num_conta_origem, num_conta_destino, valor in self.transacoes_pendentes:
            conta_origem = self._contas.get(num_conta_origem)
            conta_destino = self._contas.get(num_conta_destino)
            if conta_origem and conta_destino and valor > 0:
                if conta_origem.saldo >= valor:
                    conta_origem.saldo -= valor
                    conta_destino.saldo += valor
                    conta_origem.historico_de_operacoes.append(f"Operacao numero:  {len(conta_origem.historico_de_operacoes) + 1} Valor:  -{valor}")
                    conta_destino.historico_de_operacoes.append(f"Operacao numero:  {len(conta_destino.historico_de_operacoes) + 1} Valor:  {valor}")
                    #print(f"Transferência processada: {valor} de conta {num_conta_origem} para conta {num_conta_destino}.")
                else:
                    print(f"Saldo insuficiente para a transferência de {valor} de conta {num_conta_origem}.")
            else:
                print(f"Falha ao processar transferência de {valor} de conta {num_conta_origem} para conta {num_conta_destino}.")
        self.transacoes_pendentes.clear()

