import re

import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('VENDAS MARCELO 20-23.xlsx')


# Função para limpar os nomes
def limpar_nome(nome):
    return re.sub(r'^\d+\s*-\s*', '', nome).strip()


# Função para limpar o Documento (NF)
def limpar_documento(doc):
    return re.sub(r'^NFE--', '', doc).strip()


# Função para limpar a Descrição do Produto/Serviço
def limpar_descricao(descricao):
    return re.sub(r' -? ?-? .+$', '', descricao).replace('-', '').strip()

# Aplicar a função de limpeza nas colunas
df['VENDEDOR'] = df['VENDEDOR'].apply(limpar_nome)
df['CLIENTE'] = df['CLIENTE'].apply(limpar_nome)
df['Documento'] = df['Documento'].apply(limpar_documento)
df['Descrição do Produto/Serviço'] = df['Descrição do Produto/Serviço'].apply(
    limpar_descricao
)

# Limpar a coluna 'Código' e convertê-la para inteiro
df['Código'] = (
    pd.to_numeric(df['Código'], errors='coerce').fillna(0).astype(int)
)

# Salvar o DataFrame limpo em um novo arquivo Excel
df.to_excel('seu_arquivo_limpo.xlsx', index=False)
