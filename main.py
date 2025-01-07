# main.py
from processador_vendas import ProcessadorDeVendas

def main():
    # Caminho para o arquivo CSV
    caminho_arquivo = "vendas.csv"
    
    # Cria uma instância da classe ProcessadorDeVendas
    processador = ProcessadorDeVendas(caminho_arquivo)
    
    # Executa o pipeline e obtém o total de vendas
    total_vendas = processador.executar_pipeline()
    
    # Exibe o resultado
    print(f"Total de vendas dos produtos entregues: {total_vendas}")

main()
