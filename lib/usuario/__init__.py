import string

from lib.database import JsonDataBase
from lib.hash import Hash


class Usuario:

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.database_json = JsonDataBase()
        self.gerador_hash = Hash(self.senha)

    def carregar_cadastro_salvo(self):
        return self.database_json.read()

    def salvar_db(self, cadastro):
        self.database_json.save(cadastro) if cadastro else False

    def padronizar_nome(self):
        """Elimita todos os espaços em branco duplicados e titulariza cada palavra. Mínimo 6 caracteres"""
        nome = string.capwords(self.usuario)
        return nome if len(str(nome)) >= 6 else False

    def criar_hash_senha(self):
        """Gera números e caracteres aleatórios com tamanho de 78 embutido a senha informada"""
        return self.gerador_hash.gerador_hash()

    def verificar_existencia_cadastro(self):
        if self.database_json.read():
            for usuario_cadastrado in self.database_json.read():
                if usuario_cadastrado['usuario'] == self.padronizar_nome():
                    return True, usuario_cadastrado['usuario'], usuario_cadastrado['senha']

    def cadastrar(self):
        """Se não existir no banco de dados, será cadastrado com o nome padronizado e senha verificada"""
        if not self.verificar_existencia_cadastro():
            if self.padronizar_nome() and self.gerador_hash.verificador_senha():
                cadastro = {'usuario': self.padronizar_nome(), 'senha': self.criar_hash_senha()}
                self.salvar_db(cadastro)
            else:
                return False
        else:
            return False

    def login(self):
        try:
            condicao, usuario, senha = self.verificar_existencia_cadastro()
            if condicao and self.gerador_hash.comparador_senha(senha):
                return True
        except TypeError:
            return False


if __name__ == '__main__':
    pass
