# project_insight_house_rocket
![crop-hand-holding-house-near-coins](https://user-images.githubusercontent.com/107287165/175185016-1ac7ddca-a12a-42da-b223-46184753a414.jpg)



# 1. Problema de Negócio
A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia.
O CEO da House Rocket gostaria de maximizar a receita da empresa encontrando boas oportunidades de negócio.Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e, portanto, maior sua receita.

Portanto,uma análise exploratória foi desenvolvida para identidficar imóveis com potencial de compra e venda. Além disso, um site em cloud foi utilizado para mostrar a análise de outra maneira.
The resulting app can be accessed [here](https://kc-insights.herokuapp.com/)

# 2. Suposições de Negócio.
As seguintes suposições para este problema de negócio foram tomadas:

-> Id’s repetidos foram removidos pois foram considerados como erros na atualização do banco de dados. Foi mantido apenas o último ID nessas duplicadas devido a atualização mais recente.

-> As estações receberam muita importância no resultado final.

# Lista de Atributos
Para o processo de análise foi utilizado um dataset público hospedado no [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction).

Este dataset possui as seguintes variáveis:

|Atributos | Descrição |
|----------|-----------|
|id | Identificador de anúncio para cada propriedade. |
|date |	Data em que a propriedade ficou disponível. |
|price | O preço anunciado de cada imóvel. |
|bedrooms | Número de quartos. |
|bathrooms | O número de banheiros, sendo os valores 0,5 o indicador de um quarto com banheiro, mas sem chuveiro, já o valor 0,75 ou 3/4 representa um banheiro que contém uma pia, um vaso sanitário e um chuveiro ou banheira. |
|sqft_living | Pés quadrados do interior das casas. |
|sqft_lot |	Pés quadrados do terreno das casas. |
|floors | Número de andares. |
|waterfront | Variável indicadora para imóveis com visualização ao mar (1) ou não (0). |
|view | Um índice de 0 a 4 de quão boa era a visualização da propriedade. |
|condition |  Um índice de 1 a 5 sobre o estado das moradias, 1 indica propriedade degradada e 5 excelente. |
|sqft_above | Os pés quadrados do espaço habitacional interior acima do nível do solo. |
|sqft_basement | Os pés quadrados do espaço habitacional interior abaixo do nível do solo. |
|yr_built | Ano de construção da propriedade. |
|yr_renovated | Representa o ano em que o imóvel foi reformado. Considera o número ‘0’ para descrever as propriedades nunca renovadas. |
|zipcode | Um código de cinco dígitos, similar ao CEP, para indicar a área onde se encontra a propriedade. |
|lat | Coordenada de Latitude. |
|long | Coordenada de Longitude. |
|sqft_living15 | O tamanho médio em pés quadrados do espaço interno de habitação para as 15 casas mais próximas. |
|sqft_lot15 | Tamanho médio dos terrenos em metros quadrados para as 15 casas mais próximas. |

# 3. A solução
Para solucionar esta questão, foi elaborado alguns relatórios, o primeiro com sugestões de compra por imóvel juntamente com o valor recomendado, para o segundo relatório conterá sugestão de venda indicando os melhores momentos para venda e o valor recomendado.

A estrutura para recomendação de compras leva em consideração a mediana de preço do imóvel por região, portanto imóveis com preço abaixo da mediana, boas condições e avaliações serão os recomendados.

A estrutura utilizada para a venda de imóveis considera a mediana do preço de imóveis e a sazonalidade (temporada) do ano, estes atributos permitem recomendar vendas com base na mediana de preço da região e os melhores meses para anunciar. 

# 4. Estratégia de Solução
![image](https://user-images.githubusercontent.com/107287165/175185090-7fc87ee7-706e-4fc9-b01b-48c5728ffdc4.png)

Minha estratégia para resolver esse desafio foi:

**Step 01.** Determinar o problema de negócio

**Step 02.** Carregar e inspecionar os dados

**Step 03.** Limpeza e transformação de dados

**Step 04.** Análise exploratória

**Step 05.** Hipóteses 

**Step 06.** Resposta dos problemas de negócios

**Step 07.** Criação do app no heroku 

**Step 08.**  Conclusão

# 5. Top 5 Insights de Negócio
No processo das análises exploratórias dos dados, foram levantadas algumas hipóteses de negócio que deveriam ser validadas (ou invalidadas) a fim de trazer insights de negócio. Destaco aqui 5 Insights identificados nos dados.

**H1 - Imóveis que possuem vista para água, são 20% mais caros, na média.**

Falso. Os imóveis com vista são 211.76% mais caros que os imóveis sem vista 

**H2 - Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.**

Falso. Imóveis com data de construção menor que 1955 são 1.38% mais baratos que os imóveis construidos após 1955

**H3 - Imóveis sem porão (sqft_basement), são 40% maiores do que com porão em media.**

Hipótese Falsa. Os Imóveis sem porão são maiores em 22.78% comparados a imóveis com porão

**H4 - O crescimento do preço dos imóveis YoY (Year over Year) é de 10%**

Falso. Os imóveis listados em 2015 são mais caros em 0.18% comparados a imóveis de 2014. Como esses são os únicos anos, então conclui-se que a hipótese é falsa.

**H5  - Imóveis com 3 banheiros tem um crescimento MoM (Month over Month) de 15% em média**

Falso. Os preços aumentam e diminuem no período determinado.

**H6 - O preço da casa cai em média 30% a cada nível de condição**

Falso. O preço dos imóveis cai em média 18.50% a cada diminuição no nível de condição. 

**H7 - As casas ficam 40% mais caras a cada andar**

Falso. Média de preço dos imóveis com 3 andares é menor do que os imóveis com 2 andares.

**H8 Imóveis com boa vista ( 3 pra cima) e boas condições ( 3 pra cima ) são 40% mais caras que as casas com boas vistas( 3 pra cima )**

O preço dos imóveis em boas condições e boa vista é em média maior em 177.67 % do que os imóveis com boa vista mas em condições ruins 

**H9 - The YoY rise in price is 10%**

False. Price decreased in 2015. 

**H10 - The MoM rise in prices of houses with 3 bathroom is 15%**

False. Prices decrease and increase at the period comprised in the dataset. The months of January, February and November would be the best moment to invest in houses.



# 6. Resultados de Negócio
The main objective of this project was to answer two business questions:
1. Which houses the company should buy and at which price?
2. Once bought, when should these houses be sold and at which profit margin?

To achieve this goal, the dataset was cleaned, analysed, and some hypothesis were tested. To determine the best real state opportunities, the data was grouped based on location, housing condition and if it was located in front of water. 

These features were determined based on previous analysis, in which it was observed that location played one of the most important role in house precification. Along with general location, if a house was near a body of water, its price would also increase. In addition, for all these situations, the housing condition, specially the on lower grades, presented a proeminent effect on prices, decreasing them significantly. 

After grouping the houses on the dataset based on these conditions, the average price was calculated and if a house costed less then this average and it was in good condition, this house would be classified as suitable for purchase. After separating all suitable houses, the profit was calculated. 

This calculation was done by grouping the good real state opportunities based on all previous features and season. The average prices were calculated and if the buying price were above this average, a profit margin of 10% would be added, otherwise, the profit margin would be at 30%.

At the end of such analysis, the resulting dataset contained 10486 houses, its features, the buying and selling prices and the profit margin of each.


# 8. Conclusões
Podemos concluir que o resultado, para um primeiro ciclo de desenvolvimento, se mostra satisfatório. Foi possível após uma coleta de dados e uma análise completa, identificar alavancas de negócios, elaboração de insights e desenvolver relatórios capazes de responder as perguntas de negócio com os potenciais margens de ganho de aproximadamente 28%. 

# 9. Próximos Passos
 Um segundo ciclo de desenvolvimento é indicado para otimizar a estrutura de análise e melhorar a performance dos ganhos, também possibilita observar o problema de diferentes ângulos identificando Insights antes não observados.

**Tópicos a serem explorados:**

-> Elaborar um novo plano de recomendação de compras e vendas dos imóveis através da aplicação de Machine Learning.

-> Identificar novos Insights que possuem grande correlação para o preço.

-> Otimizar a resposta de informações disponíveis no site melhorando a experiência de usuário. 

-> Disponibilizar novos filtros para os dados gerados no site para melhorar a análise do time de negócios.
