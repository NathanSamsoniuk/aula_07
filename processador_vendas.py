import pandas as pd

class ProcessadorDeVendas:
    def __init__(self, path: str):
        """
        Inicializa o processador de vendas com o caminho do arquivo CSV.
        
        Parâmetros:
        - path (str): Caminho do arquivo CSV.
        """
        self.path = path
        self.dados = self._ler_csv()  # Lê os dados do CSV ao inicializar

    def _ler_csv(self):
        """
        Lê o arquivo CSV e retorna os dados como um DataFrame.
        """
        try:
            return pd.read_csv(self.path, encoding="utf-8")
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {self.path}")
        except Exception as e:
            raise Exception(f"Erro ao ler o arquivo: {e}")

    def filtra_produtos_entregues(self):
        """
        Filtra os produtos entregues no DataFrame.
        
        Retorno:
        - pd.DataFrame: DataFrame contendo apenas os produtos entregues.
        """
        # Converte a coluna 'entregue' para booleano, se necessário
        self.dados["entregue"] = self.dados["entregue"].astype(str)  # Garante que a coluna seja string
        return self.dados[self.dados["entregue"] == "True"]

    def somar_valores(self):
        """
        Soma os valores da coluna 'price' no DataFrame.
        
        Retorno:
        - int: Valor total somado.
        """
        return self.dados["price"].astype(int).sum()

    def executar_pipeline(self):
        """
        Executa a pipeline de processamento: lê os dados, filtra os produtos entregues
        e calcula o total das vendas.
        
        Retorno:
        - int: Valor total das vendas de produtos entregues.
        """
        produtos_entregues = self.filtra_produtos_entregues()
        return self.somar_valores()
