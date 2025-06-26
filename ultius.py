from dataset import df

def format_number(value, prefix=''):
    """Formatar números com sufixos mil/milhões"""
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'.strip()
        value /= 1000
    return f'{prefix} {value:.2f} milhões'.strip()

# Criar um gráfico onde vamos agrupar e somar
df_receita_estado = df.groupby('Local da compra')[['Preço']].sum()

# Eliminar os registros duplicados e fazer merge com coordenadas
df_receita_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(
    df_receita_estado, 
    left_on='Local da compra', 
    right_index=True
).sort_values('Preço', ascending=False)

# Execute só para mostrar
# print(df_receita_estado)