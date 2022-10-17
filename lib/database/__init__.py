import json
import os


class JsonDataBase:

    @staticmethod
    def diretory_path():
        """Cria a pasta onde ficará o arquivo.json"""
        diretory = 'db/'
        cwd = os.getcwd()  # Current Working Directory (Diretório de trabalho atual)
        full_directory_path = os.path.join(cwd, diretory)
        try:
            os.mkdir(full_directory_path)
        except FileExistsError:
            pass
        return full_directory_path

    @staticmethod
    def convert_py(format_json):
        """Converte o formato.json em formato.py"""
        return json.loads(format_json)

    @staticmethod
    def convert_json(format_py):
        """Converte o formato.py em formato.json"""
        return json.dumps(format_py)

    def file_path(self):
        """Indica o caminho em que o arquivo.json está localizado"""
        file = 'database.json'
        return f'{self.diretory_path()}{file}'

    def read(self):
        """Retorna os dados salvos em formato.py"""
        try:
            with open(self.file_path(), 'r', encoding='utf-8') as file_json:
                return json.load(file_json)
        except FileNotFoundError:
            return False

    def save(self, data):
        """Salva o primeiro registro em uma lista vazia, adicionando posteriomente novos registros"""
        try:
            # Dados recuperados, incluíndo mais registro
            lista = self.read()
            lista.append(data)
            with open(self.file_path(), 'w', encoding="utf-8") as file_json:
                json.dump(lista, file_json, indent=4, ensure_ascii=False)
        except Exception:
            # Primeiro registro, criando arquivo.json
            lista = [data]
            with open(self.file_path(), 'w', encoding="utf-8") as file_json:
                json.dump(lista, file_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    pass
