from typing import Self


class Conta:
    def __init__(self):
        self.__saldo = 0

    def sacar_money(self, dinheiro_retirado):
        dinheiro = dinheiro_retirado
        self.__saldo -= dinheiro
    
    def depositar_money(self, dinheiro_retirado):
        dinheiro = dinheiro_retirado
        self.saldo += dinheiro

    def rendimento_do_money(self, meses):
        meses = meses
        while range(meses):
            self.__saldo += self.__saldo * 0.1