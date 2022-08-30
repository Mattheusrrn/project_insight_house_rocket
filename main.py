import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')
pd.set_option('display.float_format', '{:.2f}'.format)
st.title('House Rocket Company')
st.markdown('Bem vindo a análise de dados da House Rocket. Este site tem como objetivo apresentar'
            ' os resultados construidos através do projeto de dados gerado pelo link: '
            '[House Rocket Project](https://github.com/Mattheusrrn/project_insight_house_rocket)'
            , unsafe_allow_html=True)


@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data_no_duplicates = data.drop_duplicates(subset='id', keep='last')
    data_clean = data_no_duplicates.drop(15870)
    return data_clean


def data_transform(data):
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    data['floors'] = data['floors'].astype(int)
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    data['condition_type'] = data['condition'].apply(lambda x: 'good' if x > 2 else 'bad')
    data['view_quality'] = data['view'].apply(lambda x: 'good' if x > 2 else 'bad')
    data['renovated'] = data['yr_renovated'].apply(lambda x: 'yes' if x > 0 else 'no')
    data['season'] = data['month'].apply(lambda x: 'spring' if (x >= 3) & (x <= 5) else
    'summer' if (x >= 6) & (x <= 8) else
    'fall' if (x >= 9) & (x <= 11) else
    'winter')
    data['Buy_or_not'] = 'NA'
    data['Selling'] = 'NA'
    data['Profit'] = 'NA'
    data['age_house'] = data['yr_built'].apply(lambda x: 'new' if x > 1955 else 'old')
    data['basement'] = data['sqft_basement'].apply(lambda x: 'Sim' if x > 0 else 'No')
    return data


def hypothesis(data):
    st.header('Principais Insights')
    st.markdown(
        'Para um melhor conhecimento do banco de dados, se mostrou necessário criar algumas hipóteses e verificar sua veracidade. Essa hipóteses se baseiam no comparativo de variáveis e é importante que alguma estatística esteja atrelada nesse comparativo.  Dessa forma, se criou 10 hipóteses que são mostradas nos gráficos abaixo:')

    # H1: Imóveis que possuem vista para água, são 20% mais caros, na média.
    c1, c2 = st.columns((1, 1))
    c1.subheader('Imóveis/Vista para a água')
    c1.markdown('Hipótese 1: Imóveis que possuem vista para água, são 30% mais caros, na média.')
    x = data[['waterfront', 'price']].groupby(['waterfront']).mean().reset_index()
    fig = px.bar(x, x='waterfront', y='price', labels={'waterfront': 'Vista a água', 'price': 'Preço'}
                 , color='waterfront')
    c1.plotly_chart(fig, use_container_width=True)
    c1.markdown('Falso. Os imóveis com vista são 211.76% mais caros que os imóveis sem vista')

    c2.subheader('Imóveis/Ano de construção')
    c2.markdown('Hipótese 2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')
    y = data[['age_house', 'price']].groupby('age_house').mean().reset_index()
    fig = px.bar(y, x='age_house', y='price', labels={'age_house': 'Condição do imóvel', 'price': 'Preço'}
                 , color='age_house')
    c2.plotly_chart(fig, use_container_width=True)
    c2.markdown(
        'Imóveis com data de construção menor que 1955 são 1.38% mais baratos que os imóveis construidos após 1955')

    # H3: Imóveis sem porão (sqft_basement), são 40% maiores do que com porão em media.
    c3, c4 = st.columns((1, 1))
    c3.subheader('Imóveis/Porão')
    c3.markdown('Hipótese 3: Imóveis sem porão (sqft_basement), são 40% maiores do que com porão em media.')
    z = data[['basement', 'sqft_lot']].groupby('basement').mean().reset_index()
    fig = px.bar(z, x='basement', y='sqft_lot', labels={'basement': 'Com ou sem porão?', 'price': 'Tamanho'},
                 color='basement')
    c3.plotly_chart(fig, use_container_width=True)
    c3.markdown('Hipótese Falsa. Os Imóveis sem porão são maiores em 22.78% comparados a imóveis com porão')

    # H4: O crescimento do preço dos imóveis YoY (Year over Year) é de 10%
    c4.subheader('Crescimento dos preços dos imóveis ano após ano')
    c4.markdown('Hipótese 4: O crescimento do preço dos imóveis YoY (Year over Year) é de 10%.')
    w = data[['price', 'year']].groupby('year').mean().reset_index()
    fig = px.bar(w, x='year', y='price', labels={'year': 'Ano', 'price': 'Preço'}, color='year')
    c4.plotly_chart(fig, use_container_width=True)
    c4.markdown('Hipótese Falsa.Os imóveis de 2015 são mais caros em 0.18% comparados a imóveis de 2014')

    c5, c6 = st.columns((1, 1))
    # H5: Imóveis com 3 banheiros tem um crescimento MoM (Month over Month) de 15% em média
    c5.subheader('Imóveis com 3 banheiros e seu crescimento ano após ano')
    c5.markdown('Hipotese 5: Imóveis com 3 banheiros tem um crescimento MoM (Month over Month) de 15% em média.')
    s = data[['price', 'bathrooms', 'month']].groupby(['bathrooms', 'month']).mean().reset_index()
    s1 = s[s['bathrooms'] == 3]
    fig = px.bar(s1, x='month', y='price', labels={'month': 'Mês', 'price': 'Preço'}, color='month')
    c5.plotly_chart(fig, use_container_width=True)
    c5.markdown(
        'Hipótese Falsa.Como podemos observar no gráfico, há muita variância com o resultado do mês 12 estando muito próximo do mês 1')

    # H6:  O preço da casa cai em média 30% a cada nível de condição
    c6.subheader('Queda no preço por condição')
    c6.markdown('Hipótese 6: O preço da casa cai em média 30% a cada nível de condição.')
    t = data[['price', 'condition']].groupby('condition').mean().reset_index()
    fig = px.bar(t, x='condition', y='price', labels={'condition': 'Condição do imóvel', 'price': 'Preço'},
                 color='condition')
    c6.plotly_chart(fig, use_container_width=True)
    c6.markdown('Hipótese Falsa.O preço dos imóveis cai em média 18.50% a cada nível de condição')

    c7, c8 = st.columns((1, 1))
    # H7: As casas ficam 40% mais caras a cada andar
    c7.subheader('Preço do imóvel por andar')
    c7.markdown('Hipótese 7: As casas ficam 40% mais caras a cada andar.')
    q = data[['floors', 'price']].groupby('floors').mean('price').reset_index()
    fig = px.bar(q, x='floors', y='price', labels={'floors': 'Andares', 'price': 'Preço'}, color='floors')
    c7.plotly_chart(fig, use_container_width=True)
    c7.markdown('Hipótese Falsa. Média de preço dos imóveis com 3 andares é menor do que os imóveis com 2 andares.')

    # h8 : casas com boas vistas ( 3 pra cima) e boas condições ( 3 pra cima ) são 40% mais caras que as casas com boas vistas( 3 pra cima )
    c8.subheader('Imóvel / Boa vista/ Boas condições')
    c8.markdown(
        'Hipótese 8: imóveis com boas vistas ( 3 pra cima) e boas condições ( 3 pra cima ) são 40% mais caras que as casas com boas vistas( 3 pra cima ).')
    e = data[['condition_type', 'price', 'view_quality']].groupby(
        ['condition_type', 'view_quality']).mean().reset_index()
    e1 = e[e['view_quality'] == 'good']
    fig = px.bar(e, x='condition_type', y='price', labels={'condition_type': 'Tipo de condição', 'price': 'Preço'},
                 color='condition_type')
    c8.plotly_chart(fig, use_container_width=True)
    c8.markdown(
        'Hipótese Falsa.O preço dos imóveis em boas condições e boa vista é em média maior em 177.67 % do que os imóveis com boa vista mas em condições ruins.')

    c9, c10 = st.columns((1, 1))
    # h9: imóveis com reforma são 25% mais caros
    c9.subheader('Imóvel/Reforma')
    c9.markdown('Hipótese 9: imóveis com reforma são 25% mais caros.')
    f = data[['renovated', 'price']].groupby('renovated').mean().reset_index()
    fig = px.bar(f, x='renovated', y='price', labels={'renovated': 'Reformado?', 'price': 'Preço'}, color='renovated')
    c9.plotly_chart(fig, use_container_width=True)
    c9.markdown(
        'Hipótese Falsa.O preço dos imóveis com reforma é em média maior em 43.29 % do que os imóveis sem reforma.')

    # h10: imóveis são mais caros em 10% no verão
    c10.subheader('Preço dos imóveis no verão')
    c10.markdown('Hipotese 10: imóveis com reforma são 25% mais caros.')
    g = data[['season', 'price']].groupby('season').mean().reset_index()
    fig = px.bar(g, x='season', y='price', labels={'season': 'estação', 'price': 'Preço'}, color='season')
    c10.plotly_chart(fig, use_container_width=True)
    c10.markdown('Hipótese Falsa.Os imóveis na primavera são mais caros em 0.73% do que os imóveis no verão.')

    return None


def data_buy(data):
    st.header('Relatórios')
    st.markdown('Abaixo se encontra os relatórios com análises indicando imóveis a comprar.')
    st.markdown(
        'Esse relatório foi obtido por meio de uma análise dos imóveis com preço abaixo da mediana da sua localidade e de imóveis com condições consideradas boas pela nossa tabela.')
    mediana = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
    data = pd.merge(data, mediana, on='zipcode', how='inner')
    for i in range(len(data)):
        if (data.loc[i, 'price_x'] < data.loc[i, 'price_y']) & (data.loc[i, 'condition'] >= 3):
            data.loc[i, 'Buy_or_not'] = "Buy"
        else:
            data.loc[i, 'Buy_or_not'] = "Dont Buy"
    df1 = data[data['Buy_or_not'] == 'Buy']

    df1 = df1[['id', 'zipcode', 'price_x', 'price_y', 'condition', 'Buy_or_not', 'season', 'lat', 'long']]
    df1.rename(columns={'price_x': 'price', 'price_y': 'median price'}, inplace=True)
    total = df1.shape[0]
    overall = data.shape[0]
    perc = (total / overall) * 100
    st.dataframe(df1)
    st.write(
        f'A quantidade de imóveis com condição de compra é de: {total} unidades. A quantidade corresponde a {perc:.2f}% dos dados totais inicialmente coletados.')

    return df1


def data_sell(data):
    sazonalidade = data[['price', 'zipcode', 'season']].groupby(['zipcode', 'season']).median('price').reset_index()
    df2 = pd.merge(data, sazonalidade, on=['zipcode', 'season'], how='inner')
    df2.rename(columns={'price_x': 'Buying_price', 'price_y': 'season_median'}, inplace=True)
    for i in range(len(df2)):
        if (df2.loc[i, 'Buying_price'] < df2.loc[i, 'season_median']):
            df2.loc[i, 'selling_price'] = df2.loc[i, 'Buying_price'] * 0.3 + df2.loc[i, 'Buying_price']
            df2.loc[i, 'profit_margin'] = 0.3
            df2.loc[i, 'Profit'] = df2.loc[i, 'Buying_price'] * 0.3
        else:
            df2.loc[i, 'selling_price'] = df2.loc[i, 'Buying_price'] * 0.1 + df2.loc[i, 'Buying_price']
            df2.loc[i, 'profit_margin'] = 0.1
            df2.loc[i, 'Profit'] = df2.loc[i, 'Buying_price'] * 0.1
    total1 = df2['Profit'].sum()
    total2 = df2['Buying_price'].sum()

    return df2


@st.cache(allow_output_mutation=True)
def map_opportunities(data):
    fig = px.scatter_mapbox(
        data,
        lat='lat',
        lon='long',
        color='Buy_or_not',
        size='price',
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})

    return fig


if __name__ == "__main__":
    st.sidebar.title('Encontre os melhores imóveis - House Rocket (Insights)')
    st.sidebar.markdown(
        'A House Rocket é uma plataforma digital americana que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia. Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e portanto maior sua receita.')
    st.sidebar.markdown(
        'Portanto, o meu trabalho, como estudante, de Data Scientist é responder as seguintes perguntas:')
    st.sidebar.markdown('1. Quais casas deveriam ser compradas e por qual preço?')
    st.sidebar.markdown(
        '2. Depois da compra, qual seria o melhor momento para vendê-las e qual seria o preço da venda?')

    path = 'kc_house_data.csv'

    data = get_data(path)
    data1 = data_transform(data)
    hypothesis(data1)
    data2 = data_buy(data1)

    st.header('Oportunidades Imobiliárias')
    st.write(
        'No mapa abaixo, é possível identicar todos os imóveis disponíveis para compra. Em azul, encontramos os imóveis que foram classificados como boa opção de compra. Resultados estes, baseados na condição do valor de compra do imóvel. Mais abaixo, encontraremos a tabela com os imóveis classificados com boas recomendações de compra e com algumas atribuições para análises.')
    fig = map_opportunities(data2)
    st.plotly_chart(fig)
    st.header('Relatórios de Sazonalidades e possíveis lucros')
    st.markdown(
        'A partir do relatório acima e do mapa detalhado acima, podemos observar bem os imóveis com possibilidade de compra. No entanto, é necessário ter uma visão detalhada sobre os lucros que esses imóveis podem proporcionar para satisfazer os desejos da House Rocket. ')
    st.markdown(
        ' Diante disso,uma tabela com sugestão de preço de venda se faz necessária. Assim, a sazonalidade foi levada em consideração para o preço final visto que os imóveis que estão com preço abaixo da mediana da estação poderá ser colocada a venda com 30% a mais no preço. Em ordem, é exibido o id identificador do imóvel, o CEP, o preço de compra, a mediana dos preços de imóveis do mesmo CEP, a condição que o imóvel se encontra, status de compra que nesse caso sempre será positivo, a estação do ano, as coordenadas geográficas, o preço mediano da estação que o imóvel foi colocado a venda, o preço que se sugere a venda e o lucro.')
    selling = data_sell(data2)
    column_selector = st.multiselect('Filtre as informações, para exibi-las, como desejar:', selling.columns.tolist())

    if column_selector == []:
        data_set = selling
    else:
        data_set = selling[column_selector]

    st.write(data_set)
