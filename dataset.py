import json
import pandas as pd

# Criar uma variável de inserir dados
baseDeDados = open('dados/vendas.json', 'r', encoding='utf-8')

# Abrir com json
dadosTratados = json.load(baseDeDados)

# Criar DataFrame
df = pd.DataFrame.from_dict(dadosTratados)

# Imprimir dados
print(df)

# Fechar arquivo
baseDeDados.close()