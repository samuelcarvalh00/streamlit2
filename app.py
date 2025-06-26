import streamlit as st
import plotly.express as px 


#importar o ultius
from ultius import format_number


#nosso df que criamos 
    
from dataset import df

#importar o app
from grafico import grafico_map_estado


#colocar o layout da pagina

st.set_page_config(layout='wide')

st.title("Dashboard de Vendas ✉︎ ")
    #criar abas
abaum, abadois, abatres =  st.tabs(['Dataset', 'Receita', 'Vendedores'])    

with abaum:
        st.dataframe(df)
        
        #metricas
        with abadois:
            colunaum, colunadois = st.columns(2)
            with colunaum:
                #coletar o preço total do dataset
                st.metric('Receita Total', format_number(df['Preço'].sum()))
                st.plotly_chart(grafico_map_estado, use_container_width=True)
            with colunadois:
                st.metric('quantidade de vendas', format_number(df.shape[0]))
                
with abatres:
    st.subheader("Resumo por Vendedor")
    
    col1, col2 = st.columns(2)

    
with col1:
    with col1:
        receita_por_vendedor = df.groupby("Vendedor")["Preço"].sum().sort_values(ascending=False).reset_index()
    # O argumento 'text_auto' não é válido para px.scatter
    fig_receita = px.scatter(receita_por_vendedor, x="Vendedor", y="Preço", title="Receita por Vendedor", template="plotly_dark")
    st.plotly_chart(fig_receita, use_container_width=True)

with col2:
    vendas_por_vendedor = df["Vendedor"].value_counts().reset_index()
    vendas_por_vendedor.columns = ["Vendedor", "Quantidade de Vendas"]
    fig_vendas = px.pie(vendas_por_vendedor, values="Quantidade de Vendas", names="Vendedor", title="Participação nas Vendas", hole=0.4, template="simple_white")
    st.plotly_chart(fig_vendas, use_container_width=True)


st.subheader("Média da Avaliação por Vendedor (Gráfico de Linhas)")
avaliacao_media_por_vendedor = df.groupby("Vendedor")["Avaliação da compra"].mean().sort_values(ascending=False).reset_index()
fig_avaliacao_linha = px.line(avaliacao_media_por_vendedor, x="Vendedor", y="Avaliação da compra",
                             title="Média da Avaliação por Vendedor", markers=True, template="ggplot2")
st.plotly_chart(fig_avaliacao_linha, use_container_width=True)