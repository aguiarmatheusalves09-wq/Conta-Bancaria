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

    def ver_money(self):
        money = self.__saldo
        return money

    def rendimento_do_money(self, meses):
        meses = meses
        render = 0
        while range(meses):
            render += self.__saldo * 0.1
            return render