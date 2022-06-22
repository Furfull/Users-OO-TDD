from typing import List
from datetime import datetime
from dateutil.relativedelta import relativedelta
import uuid
from import_basepath import *

class Usuario:

    def __init__(self, nome: str, email: str, senha: str, celular1: str, data_nasc: datetime, cpf: str, celular2: str = None, genero: Genero = Genero.NAO_DECLARADO):
        if nome == "":
            raise Exception (CAMPO_VAZIO)
        if len(nome) > TAMANHO_MAX_NOME:
            raise Exception (CAMPO_LONGO)
        if email == "":
            raise Exception (CAMPO_VAZIO)
        if len(email) > TAMANHO_MAX_EMAIL:
            raise Exception (CAMPO_LONGO) 
        if senha == "":
            raise Exception (CAMPO_VAZIO)
        if len(senha) > TAMANHO_MAX_SENHA:
            raise Exception (CAMPO_LONGO) 
        if celular1 == "":
            raise Exception (CAMPO_VAZIO)
        if len(celular1) != TAMANHO_MAX_CELULAR:
            raise Exception (CAMPO_INVALIDO)
        try:
            if len(celular2) != TAMANHO_MAX_CELULAR:
                raise Exception (CAMPO_INVALIDO) 
        except:
            pass
        if data_nasc == "":
            raise Exception (CAMPO_VAZIO)
        if isinstance(data_nasc, datetime) == False:
            raise Exception (CAMPO_INVALIDO)
        if data_nasc >= (datetime.now() - relativedelta(years=16)):
             raise Exception (USUARIO_MENOR)
        if cpf == "":
            raise Exception (CAMPO_VAZIO)
        self.ID = str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.senha = senha
        self.celular1 = celular1
        self.celular2 = celular2
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.genero = genero

