"""
DOMÍNIO: Gestão de Conta Bancária
 
CLASSES DO PROJETO
    ContaBancaria: classe de domínio que representa a conta e valida os dados.
    TitularInvalidoError e SaldoInvalidoError: exceções personalizadas.
    ContaFactory: fábrica que cria os objetos da conta.
    BancoRepository: repositório em memória para guardar as contas.
    JanelaBancaria: a interface gráfica em Tkinter.
 
O QUE VAI SER VALIDADO E AS EXCEÇÕES
    Nome do titular: TODO (definir o que conta como "3 letras")
    Lança: TitularInvalidoError
    Saldo inicial: TODO (definir se zero é inválido ou só negativo)
    Lança: TODO (quem converte texto em número? qual exceção sai para "abc"?)
 
PADRÕES DE PROJETO ESCOLHIDOS
    Simple Factory: TODO (por quê)
    Singleton: TODO (por quê)
 
USO DE FERRAMENTAS DE IA
    Usei para: TODO
    Links das conversas: TODO (colar os links reais)
"""

import tkinter as tk
from tkinter import messagebox

class ContaInvalidaError(Exception):
    pass

class TitularInvalidoError(ContaInvalidaError):
    pass

class SaldoInvalidoError(ContaInvalidaError):
    pass


class ContaBancaria:
    def __init__(self, titular, saldo) -> None:
        if len(titular.strip()) < 3:
            raise TitularInvalidoError("O nome precisa ter pelo menos 3 letras")
        self.titular = titular

        if saldo <= 0:
            raise SaldoInvalidoError("O saldo inicial precisa ser maior que 0")
        self.saldo = saldo
        ...

class ContaFactory:
    @staticmethod
    def criar(titular_texto, saldo_texto):
        try:
            saldo = float(saldo_texto.replace(",","."))
        except ValueError:
            raise SaldoInvalidoError("O saldo precisa ser um número")
        return ContaBancaria(titular_texto, saldo)
        ...

class BancoRepository:
    _instancia = None
    _contas: list

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._contas = []
        return cls._instancia
        ...
    
    def adicionar(self, conta):
        self._contas.append(conta)
        ...

    def listar(self):
        return list(self._contas)
        ...

class JanelaBancaria(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conta Bancária")
        self._montar_formulario()

    def _montar_formulario(self):
        tk.Label(self, text="Titular:").grid(row = 0, column = 0, padx = 5, pady = 5)
        self.entrada_titular = tk.Entry(self)
        self.entrada_titular.grid(row = 0, column = 1, padx = 5, pady = 5)

        tk.Label(self, text="Saldo:").grid(row = 1, column = 0, padx = 5, pady = 5) 
        self.entrada_saldo = tk.Entry(self)
        self.entrada_saldo.grid(row = 1, column = 1, padx = 5, pady = 5)

        tk.Button(self, text="Criar conta", command=self._ao_clicar_criar).grid(row = 2, column = 0, padx = 5, pady = 5)
        ...

    def _ao_clicar_criar(self):
        try:
            conta = ContaFactory.criar(self.entrada_titular.get(), self.entrada_saldo.get())
            BancoRepository().adicionar(conta)
            total = len(BancoRepository().listar())
            messagebox.showinfo("Sucesso", f"Conta de {conta.titular} criada! Total: {total}")
        except ContaInvalidaError as erro:
            messagebox.showerror("Dados inválidos", str(erro))
        ...

if __name__ == "__main__":
    JanelaBancaria().mainloop()

"""
AUTOAVALIAÇÃO
    Critérios atingidos / não atingidos: TODO
    Trecho que deu mais trabalho e como resolveu: TODO
    As consequências escritas para cada padrão apareceram no código?: TODO
    IA: em que ajudou e em que atrapalhou: TODO
"""