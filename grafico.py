import plotly.express as px  
from ultius import df_receita_estado

grafico_map_estado = px.scatter_geo(
    df_receita_estado,
    lat = 'lat',
    lon = 'lon',
    scope='south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)
    