Média: Representa o valor central dos dados. É calculada pela soma de todos os valores e divisão pela quantidade de valores.

A função np.mean() é utilizada para calcular a média em listas do NumPy.

A função dados["IDADE"].mean() calcula a média da coluna "IDADE" no Pandas.

Podemos calcular também a média ponderada, em que cada valor tem um peso diferente. Por exemplo, vamos imaginar que estamos fazendo uma votação para definir o preço de um produto em uma empresa, mas os votos dos diretores da empresa têm um peso maior. Então para isso temos uma coluna com os pesos dos votos e outra com o preço. O cálculo da média ponderada fica assim:  

media_ponderada = (df[Preco] * df['Pesos']).sum() / df['Pesos'].sum()

Mediana: Valor central dos dados ordenados. Menos afetada por valores extremos ("outliers").

A função np.median() calcula a mediana em listas do NumPy.

A função dados["IDADE"].median() calcula a mediana da coluna "IDADE" no Pandas.

Moda: Valor que aparece mais frequentemente nos dados.

A função dados["IDADE"].mode() calcula a moda da coluna "IDADE" no Pandas.

Desvio Padrão: Mede a dispersão dos dados em relação à média.

A função dados["IDADE"].std() calcula o desvio padrão da coluna "IDADE" no Pandas.

Min e Max: Retornam o menor e o maior valor da coluna, respectivamente.

A função dados["IDADE"].min() retorna o valor mínimo da coluna "IDADE" no Pandas.

A função dados["IDADE"].max() retorna o valor máximo da coluna "IDADE" no Pandas.