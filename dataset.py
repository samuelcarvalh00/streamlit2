import json
import pandas as pd

#criar uma variavel de inserir dados
baseDeDados = open('dados/vendas.json')

#abrir com json
dadosTratados = json.load(baseDeDados)

#exibir
#prints(dadosTratados)
df  = pd.DataFrame.from_dict(dadosTratados)
#imprimir dados
print(df)
#fechar
baseDeDados.close() 