# Processador de Vendas

Um projeto simples para processar e analisar vendas a partir de um arquivo CSV. O objetivo é calcular o total de vendas de produtos que foram entregues.

---

## Estrutura do Projeto

- processador_vendas.py: Contém a classe `ProcessadorDeVendas` responsável por carregar, filtrar e calcular os dados do arquivo CSV.  
- main.py: Arquivo principal que utiliza a classe `ProcessadorDeVendas` para executar o pipeline e exibir o resultado final.  
- vendas.csv: Exemplo de arquivo CSV contendo os dados de vendas.  
- requirements.txt: Arquivo contendo as dependências necessárias para o funcionamento do projeto.  

---

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2.  **Instale as dependências: Certifique-se de ter o Python instalado (versão 3.8 ou superior).**
pip install -r requirements.txt

3.  **Execute o projeto:**
python main.py

## Tecnologias Utilizadas

- Python: Linguagem principal do projeto.
- Pandas: Biblioteca para manipulação e análise de dados.

## Dependências

O projeto utiliza apenas a biblioteca pandas. O arquivo requirements.txt contém:

pandas==2.0.3

## Funcionalidades

1. Leitura do CSV: Carrega os dados do arquivo especificado.
2. Filtragem de Dados: Considera apenas os produtos com status "Entregue".
3. Cálculo Total: Soma as quantidades dos produtos entregues.