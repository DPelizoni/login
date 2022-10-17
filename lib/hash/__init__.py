import random
import string


class Hash:

    def __init__(self, senha):
        self.senha = senha

    @staticmethod
    def gerador_caracteres():
        """Gera uma lista de 6 ítens com 6 caracteres"""
        return [''.join(random.choice(string.ascii_letters) for _ in range(6)) for _ in range(6)]

    @staticmethod
    def gerador_digitos():
        """Gera uma lista de 6 ítens com 6 digítos"""
        return [''.join(random.choice(string.digits) for _ in range(6)) for _ in range(6)]

    @staticmethod
    def desempacotador_hash(hash_salvo):
        """A senha bruta de 6 ítens, estão nos índices [12, 25, 38, 51, 64, 77]. Total do hash 78 itens"""
        indice_senha_empacotadas = [12, 25, 38, 51, 64, 77]
        return ''.join([hash_salvo[i] for i in indice_senha_empacotadas])

    def verificador_senha(self):
        """6 é o tamanho exigido para a senha"""
        return True if len(self.senha) == 6 else False

    def empacotador_hash(self):
        """Cria uma tupla unindo os caracteres, digítos e a senha original"""
        if self.verificador_senha():
            try:
                return zip(self.gerador_caracteres(), self.gerador_digitos(), self.senha)
            except TypeError:
                return False

    def gerador_hash(self):
        """Hash de 78 ítens após empacotamento"""
        if self.empacotador_hash():
            return ''.join([f'{i[0]}{i[1]}{i[2]}' for i in self.empacotador_hash()])
        else:
            return False

    def comparador_senha(self, hash_salvo):
        return True if self.desempacotador_hash(hash_salvo) == self.senha else False


if __name__ == '__main__':
    pass
